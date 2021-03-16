from catdog.views import catdog, cat, dog
from django.urls import path

urlpatterns = [
    path('catdog', catdog, name='catdog'),
    path('cat', cat, name='cat'),
    path('dog', dog, name='dog'),
]
