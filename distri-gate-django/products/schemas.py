from ninja import ModelSchema
from products.models import Product, ProductVariant
from pydantic import BaseModel


class ProductVariantSchema(ModelSchema):
    class Meta:
        model = ProductVariant
        fields = ('id',
                  'group',
                  'type',
                  'name',
                  'variant_description',
                  
                  'price_amount',
                  'price_currency_code',
                  'price_currency_symbol',
                  'variant_image',
                  'variant_color',
                  'variant_thumbnail',
                  'supply_quantity')




class ProductSchema(ModelSchema):
    variations: list[ProductVariantSchema] = []
    class Meta:
        model = Product
        fields = ('id', 'title','description','category' , 'variations', 'seller', 'default_variant')





class ProductInput(BaseModel):
    temporary_id:           str
    title:                  str
    category:               str   | None = ''
    variations:             list['VariantInput'] = []



class VariantInput(BaseModel):
    temporary_id:           str
    name:                   str
    type:                   str   | None  = 'NAME_MODE'
    variant_image:          bytes | None  = None
    variant_image_name:     str   | None  = None
    variant_color:          str   | None  = None
    price_amount:           float
    price_currency_code:    str
    price_currency_symbol:  str
    variation_description:  str   | None
    supply_quantity:        int
    is_default:             bool





