from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf1.views import APIProductsViewSet

router = DefaultRouter()
router.register('products', APIProductsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
