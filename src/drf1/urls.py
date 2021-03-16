from django.urls import path
from drf1.views import api_products, api_products_detailed

urlpatterns = [
    path('product/', api_products, name='products'),
    path('product/<int:pk>',
         api_products_detailed,
         name='products_det'),
]