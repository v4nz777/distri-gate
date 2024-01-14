from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    address = models.ManyToManyField('Address', blank=True)
    address_current = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, related_name='current_address', blank=True)
    full_name = models.CharField(max_length=99, blank=True, null=True)
    contact_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.username
    
    def save(self, *args, **kwargs) -> None:
        self.assign_full_name()
        return super().save(*args,**kwargs)
    
    def assign_full_name(self) -> None:
        if self.first_name and self.last_name:
            self.full_name = f'{self.first_name} {self.last_name}'
        else:
            self.full_name = None
       





class Address(models.Model):
    id = models.AutoField(primary_key=True)
    address_line = models.CharField(max_length=256, blank=True, null=True)
    street = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    full_address_string = models.CharField(max_length=500, blank=True, null=True)
    resident = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="resident")
    
    class Meta:
        verbose_name_plural = "Adresses"

    def __str__(self) -> str:
        return self.full_address_string

    def save(self, *args, **kwargs) -> None:
        self.assign_full_string()
        return super().save(*args, **kwargs)
    
    def assign_full_string(self)->None:
        self.full_address_string = f'{self.address_line}, {self.street}, {self.city}, {self.province}, {self.country}, {self.postal_code}'




class UsedToken(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=500)





    


