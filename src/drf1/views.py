from drf1.models import Product
from drf1.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET'])
def api_products_detailed(request, pk):
    if request.method == 'GET':
        products = Product.objects.get(pk=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
