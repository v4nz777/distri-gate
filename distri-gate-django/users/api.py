from ninja import NinjaAPI
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404
from users.models import User, UsedToken, Address
from users.schemas import UserSchema, PrivateUserSchema, AddressIn
from distrigate.security import generate_jwt_token,require_token, whitelist_tokens_from_user
import json




app = NinjaAPI(urls_namespace='users')


@app.post('login/')
def login(request:HttpRequest)->JsonResponse:
    """Returns current `access_token` and clear the blacklisted tokens from user"""
   
    if request.method == "POST":
        decoded_body = request.body.decode('utf-8')
        data = json.loads(decoded_body)
        username = data['username']
        password = data['password']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({"message":f"User: {username} not found"})
        
        is_authenticated = user.check_password(password)

        if not is_authenticated:
            return JsonResponse({"message":"Wrong credentials, try again!"}, status=401)
        
        # By whitelisting the previous used cookies, saving database space, these tokens could be expired anyway.
        whitelist_tokens_from_user(user) 
        

        token = generate_jwt_token(username)
        return JsonResponse({"access_token":token},status=200)



@app.post('logout/')
@require_token
def logout(request:HttpRequest)->JsonResponse:
    """Add `access_token` to blacklist, By blacklisting the used token, user data is safe after logout"""
    
    token_from_headers:str = request.headers.get('Authorization')
    token = token_from_headers.split(' ')[1]
    user = request.user

    data = json.loads(request.body)
    requestor = User.objects.get(username=data['username'])

    if requestor != user:
        return JsonResponse({'message': 'User cannot logout other user'}, status=401)

    used = UsedToken.objects.create(access_token=token, owner=user)
  
    return JsonResponse({'message': 'Token revocation successful'}, status=200)




@app.get('get_users/', response=list[UserSchema])
def get_users(request:HttpRequest)->list[User]:
    return User.objects.all()




@app.get('get_user/{username}', response=UserSchema)
def get_user(request:HttpRequest,username:str)->User:
    
    user = get_object_or_404(User,username=username)

    return user



@app.get('get_private_user/{username}', response=PrivateUserSchema)
@require_token
def get_private_user(request:HttpRequest,username:str)->User:
  
    try:
        user = User.objects.get(username=username)

    except User.DoesNotExist:
        return JsonResponse({'message': f'{username} not found, may be deleted from the database!'},status=404)
    
    else:
        if request.user != user:
            message = 'Unauthorize access! You are not allowed to access this user'
            return JsonResponse({'message':message}, status_code=403)
        else:
            return user

@app.post('register_user/', response=PrivateUserSchema)
def register_user(request:HttpRequest)->User:
    if request.method == "POST":
        decoded_body = request.body.decode('utf-8')
        data = json.loads(decoded_body)
        username = data['username']
        password = data['password']
        email = data['email']


        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            return JsonResponse({'message': 'Successfully created user!'},status=200)
        except:
            return JsonResponse({'message': f'{username} not found, may be deleted from the database!'},status=404)


        


@app.post('change_current_address', response=PrivateUserSchema)
@require_token
def change_current_address(request:HttpRequest):
    try:
        data = json.loads(request.body)
        address = get_object_or_404(Address, id=data['address_id'])
        user:User = request.user
        user.address_current = address
        user.save()

    except Address.DoesNotExist:
        return JsonResponse({'message': 'Address does not exist'}, status=404)
    
    except User.DoesNotExist:
        return JsonResponse({'message': 'User does not exist'}, status=404)
    
    else:
        return user




@app.post('add_new_address/', response=PrivateUserSchema)
@require_token
def add_new_address(request:HttpRequest):
   
    user:User = request.user
    data = json.loads(request.body)
    print(data)
    _address_in:AddressIn = AddressIn(**data)
    new_address:Address = Address.objects.create(
        address_line    = _address_in.form_address_line,
        street          = _address_in.form_street,
        city            = _address_in.form_city,
        country         = _address_in.form_country,
        province        = _address_in.form_province,
        postal_code     = _address_in.form_postal_code,
        contact_person  = _address_in.form_contact_person,
        contact         = _address_in.form_contact
    )

    try:
        
        user.address.add(new_address)
        user.address_current = new_address
        user.save()
    
    except User.DoesNotExist:
        
        return JsonResponse({'message': 'User does not exist'}, status=404)
    
    except Address.DoesNotExist:
        
        return JsonResponse({'message': 'Address does not exist'}, status=404)
    else:
        return user


   