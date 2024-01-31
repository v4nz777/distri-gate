from django.shortcuts import get_object_or_404

from ninja import NinjaAPI
from users.models import User

from products.models import Product, ProductVariant
from products.schemas import ProductSchema, ProductVariantSchema
from products.schemas import ProductInput, VariantInput
from products.utils import transform_product_input_data

from distrigate.security import require_token
from django.http import HttpRequest
from django.core.files.base import ContentFile

from io import BytesIO


app = NinjaAPI(urls_namespace='products')




@app.get('get_products/', response=list[ProductSchema])
def get_products(request:HttpRequest):
    return Product.objects.all()



@app.get('get_product/{id}', response=ProductSchema)
def get_product(request:HttpRequest,id:int):
    product = get_object_or_404(Product, id=id)
    return product



@app.post('add_new_product', response=list[ProductSchema])
# @require_token
def add_new_product(request:HttpRequest):
    
    
    product_input:ProductInput = transform_product_input_data(request)
    
    # user:User = request.user
    user = User.objects.first()

    new_product = Product.objects.create(
        title = product_input.title,
        category = product_input.category,
        seller = user
    )

    for variant in product_input.variations:
        # Initiating new variant
        new_variant = ProductVariant.objects.create(
            group = new_product,
            type  = variant.type,
            name  = variant.name,
            variant_description = variant.variation_description,
            price_amount  = variant.price_amount,
            price_currency_code    = variant.price_currency_code,
            price_currency_symbol  = variant.price_currency_symbol
        )
   
        # Add the image to the variant
        if variant.variant_image != b'':
            new_variant.variant_image.save(
                variant.variant_image_name,
                ContentFile(variant.variant_image,variant.variant_image_name),
                save=True)

        # Add variant to product
        new_product.variations.add(new_variant)
    
    new_product.save()
    return Product.objects.all()

    
