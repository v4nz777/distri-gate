from django.contrib import admin
from django.urls import path
from products.api import app as products_api
from users.api import app as users_api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', products_api.urls, name='products'),
    path('api/users/', users_api.urls, name='users'),
]
