from drf1.models import Product
from drf1.serializers import ProductSerializer
from django.http import JsonResponse


def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
