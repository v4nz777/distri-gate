from __future__ import annotations
from collections.abc import Iterable
from django.db import models
from django_extensions.db.fields import AutoSlugField, ShortUUIDField,CreationDateTimeField
from PIL import Image, ImageFilter
from storages.backends.s3boto3 import S3Boto3Storage
from io import BytesIO
from django.core.files.base import ContentFile



class Product(models.Model):
    id = ShortUUIDField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=499, blank=True, null=True)
    category = models.CharField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title')
    variations = models.ManyToManyField('ProductVariant', default=[], related_name='product_variations', blank=True)
    default_variant = models.ForeignKey('ProductVariant', on_delete=models.SET_NULL, blank=True, null=True, related_name='default_variant')
    seller = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='seller')

    def __str__(self) -> str:
        return f"{self.title}  ({self.slug})"
    

    def refresh_default_variant(self)-> None:
        variations:list[ProductVariant] = self.variations
        if self.default_variant and self.default_variant_has_supply():
            return
        
        for variant in variations:
            if self.set_default_variant(variant):
                break
            else:
                continue


    def set_default_variant(self, new_default:ProductVariant)-> ProductVariant| None:
        if new_default.supply_quantity > 0:
            self.default_variant = new_default
            self.save()
            return self.default_variant
        else:
            return None
    
    
    def default_variant_has_supply(self) -> bool:
        return self.default_variant.supply_quantity > 0
        


    


class ThumbnailStorage(S3Boto3Storage):
    location = 'product_thumbnails'

class ProductVariant(models.Model):
    
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Product, on_delete=models.CASCADE ,related_name='variation_group')
    group_slug = AutoSlugField(populate_from='group')
    variant_description = models.CharField(max_length=499, blank=True, null=True)
    type = models.CharField(max_length=200, default='NAME_MODE') # OPTIONS ARE: 'NAME_MODE' | 'THUMBNAIL_MODE' | 'COLOR_MODE'

    name = models.CharField(max_length=200)
    variant_image = models.ImageField(upload_to='variant_image', null=True, blank=True)
    variant_color = models.CharField(max_length=50, blank=True, null=True)
    variant_thumbnail = models.ImageField(storage=ThumbnailStorage(), null=True, blank=True)
    
    price_amount = models.IntegerField(default=0)
    price_currency_code = models.CharField(max_length=10)
    price_currency_symbol = models.CharField(max_length=10)

    supply_quantity = models.IntegerField(default=1)

    

    def __str__(self) -> str:
        return f'{self.group_slug} -> {self.name}'
    

    def save(self, *args, **kwargs) -> None:

        if self.variant_image:
            self.create_thumbnail()

        super().save( *args, **kwargs)
    

    

    def create_thumbnail(self):
        
        # Open the image file
        image_path = self.variant_image
        img = Image.open(image_path)

        # Specify the desired width or height
        desired_width = 100
        desired_height = 100

        # Calculate the aspect ratio
        aspect_ratio = img.width / img.height

        # Calculate the new dimensions while maintaining the aspect ratio
        if img.width > img.height:
            new_width = desired_width
            new_height = int(desired_width / aspect_ratio)
        else:
            new_height = desired_height
            new_width = int(desired_height * aspect_ratio)

        # Resize the image
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Save the thumbnail to BytesIO
        thumbnail_io = BytesIO()
        img.save(thumbnail_io, format='PNG')  # Adjust format as needed
        thumbnail_io.seek(0)
        
        # Set the model's thumbnail field
        filename = f'{new_width}x{new_height}_{self.variant_image.name.replace('/','_')}'
        self.variant_thumbnail.save(filename, ContentFile(thumbnail_io.read(),filename), save=False)




class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='rater')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_to_rate')
    rating = models.IntegerField(default=5)
    date_rated = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)



class Promo(models.Model):
    id = models.AutoField(primary_key=True)
    promo_products = models.ManyToManyField(Product, related_name='promo_products', blank=True)
    promo_code = models.CharField(max_length=200, blank=True)

    discount_mode = models.CharField(max_length=20, default='PERCENT_MODE', blank=True)
    discount_percent = models.IntegerField(default=0, null=True)
    discount_amount = models.IntegerField(default=0, null=True)
    
    validity_date_start = models.DateTimeField(blank=True, null=True)
    validity_date_end = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    




class OrderItem(models.Model):
    id = models.CharField(max_length=200, primary_key=True) # GENERATED BY FRONTEND
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')

    def __str__(self) -> str:
        return self.id




class Transaction(models.Model):
    id = ShortUUIDField(primary_key=True)
    orders = models.ManyToManyField(OrderItem)
    successful = models.BooleanField(default=False)
    created = CreationDateTimeField(null=True)
    