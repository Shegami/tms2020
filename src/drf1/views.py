from drf1.models import Product
from drf1.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet


class APIProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
