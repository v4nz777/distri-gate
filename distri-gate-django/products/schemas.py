from ninja import ModelSchema
from products.models import Product


class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        fields = ('id', 'title','description','price','image','category','rating')



