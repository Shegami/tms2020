from rest_framework import serializers
from drf1.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'quantity', 'comment')
