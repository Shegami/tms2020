from django.urls import path
from drf1.views import api_products

urlpatterns = [
    path('product', api_products, name='products'),
]