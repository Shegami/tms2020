from drf1.models import Product
from drf1.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView


class APIProducts(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class APIProductDetailed(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
