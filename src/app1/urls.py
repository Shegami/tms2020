from django.urls import path
from app1.views import full_form

urlpatterns = [
    path('full_form', full_form, name='full-form')
]