from django.urls import path
from drf1.views import APIProducts, APIProductDetailed
urlpatterns = [
    path('products/', APIProducts.as_view(), name='products'),
    path('product/<int:pk>',
         APIProductDetailed.as_view(),
         name='product_det'),
]