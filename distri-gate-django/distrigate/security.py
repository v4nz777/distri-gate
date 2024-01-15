import jwt
from datetime import datetime, timedelta
from django.http import JsonResponse,HttpRequest
from django.conf import settings
from users.models import User, UsedToken
import functools


def generate_jwt_token(user_id)->str:
    """Payload contains username as `user_id`, expiration as `exp` and issued as `iat`"""
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=settings.JWT_TOKEN_EXPIRATION_DAYS),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


def whitelist_tokens_from_user(user:User)->None:
    tokens_from_user = UsedToken.objects.filter(owner=user)
    tokens_from_user.delete()


def require_token(function):
    """If token is, `request.user` will become the logged `User` instead of`AnonymousUser`"""
   
    @functools.wraps(function)
    def wrapper(request:HttpRequest, *args, **kwargs):
        
        if not request.headers.get("Authorization"):
            return JsonResponse({"message":"Cannot Find Token"}, status=401)
    
        bearer_token:str = request.headers.get("Authorization")
        token = bearer_token.split(' ')

        if token[0] != 'Bearer':
            return JsonResponse({"message":"Wrong token type must be Bearer!"}, status=400)
        
        
        try:
            decoded_data = jwt.decode(token[1],settings.SECRET_KEY,algorithms=['HS256'])
            request.user = User.objects.get(username=decoded_data['user_id'])
        

        except jwt.DecodeError:
            return JsonResponse({"message":"Wrong token!"}, status=403)
        
        except jwt.ExpiredSignatureError:
            return JsonResponse({"message":"Token expired!"}, status=403)
        
        except User.DoesNotExist:
            return JsonResponse({'message':f'User does not exist!'}, status=404)

        else:
            blacklist = UsedToken.objects.filter(access_token=token[1], owner=request.user)
            if blacklist.exists():
                return JsonResponse({"message":"Blacklisted token!"}, status=403)
            
            return function(request, *args, **kwargs)

        
    return wrapper