from django.shortcuts import get_object_or_404

from ninja import NinjaAPI
from products.models import Product
from products.schemas import ProductSchema
from distrigate.security import require_token

app = NinjaAPI(urls_namespace='products')




@app.get('get_products/', response=list[ProductSchema])
def get_products(request):
    return Product.objects.all()



@app.get('get_product/{id}', response=ProductSchema)
def get_product(request,id:int):
    product = get_object_or_404(Product, id=id)
    return product