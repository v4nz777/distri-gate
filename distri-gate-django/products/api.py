from django.shortcuts import get_object_or_404

from ninja import NinjaAPI
from users.models import User

from products.models import Product, ProductVariant
from products.schemas import ProductSchema, ProductVariantSchema
from products.schemas import ProductInput, VariantInput
from products.utils import transform_product_input_data, save_new_product, update_product

from distrigate.security import require_token
from django.http import HttpRequest, JsonResponse


from io import BytesIO


app = NinjaAPI(urls_namespace='products')




@app.get('get_products/', response=list[ProductSchema])
def get_products(request:HttpRequest):
    return Product.objects.all()



@app.get('get_product/{id}', response=ProductSchema)
def get_product(request:HttpRequest,id:str):
    product = get_object_or_404(Product, id=id)
    return product



@app.post('add_or_update_product', response=ProductSchema)
# @require_token
def add_or_update_product(request:HttpRequest):
    
    product_input:ProductInput = transform_product_input_data(request)
    
    # user:User = request.user
    user = User.objects.first()

    if not user.is_superuser:
        return JsonResponse({'message': 'Must be a superuser to access'}, status=401)
    
    
    try:
        product = Product.objects.get(id=product_input.temporary_id)
        update_product(product,product_input)

    except Product.DoesNotExist:
        product = save_new_product(product_input,user)
    
    finally:
        return product

    
