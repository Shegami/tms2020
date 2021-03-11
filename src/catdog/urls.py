from catdog.views import catdog
from django.urls import path

urlpatterns = [
    path('catdog', catdog, name='catdog')
]