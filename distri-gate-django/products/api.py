from django.shortcuts import get_object_or_404

from ninja import NinjaAPI
from users.models import User

from products.models import Product, ProductVariant
from products.schemas import ProductSchema, ProductVariantSchema
from products.schemas import ProductInput, VariantInput

from distrigate.security import require_token
from django.http import HttpRequest
import json

app = NinjaAPI(urls_namespace='products')




@app.get('get_products/', response=list[ProductSchema])
def get_products(request:HttpRequest):
    return Product.objects.all()



@app.get('get_product/{id}', response=ProductSchema)
def get_product(request:HttpRequest,id:int):
    product = get_object_or_404(Product, id=id)
    return product



@app.post('add_new_product/', response=list[ProductSchema])
@require_token
def add_new_product(request:HttpRequest):
    user:User = request.user
    
    data = json.loads(request.body)
    product_input = ProductInput(**data)


    new_product = Product.objects.create(
        title = product_input.title,
        description = product_input.description,
        category = product_input.category,
        image = product_input.image,
        variations = []
    )

    for variant in product_input.variations:
        new_variant = ProductVariant.objects.create(
            group = new_product,
            type  = variant.type,
            name  = variant.name,
            variant_image = variant.variant_image,
            variant_description = variant.variation_description,
            price_amount  = variant.price_amount,
            price_currency_code    = variant.price_currency_code,
            price_currency_symbol  = variant.price_currency_symbol
        )

        new_product.variations.add(new_variant)
    
    new_product.save()
    return Product.objects.all()

    
