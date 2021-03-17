from drf1.models import Product
from drf1.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_products_detailed(request, pk):
    if request.method == 'GET':
        products = Product.objects.get(pk=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
