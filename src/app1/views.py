from django.http import HttpResponse
from datetime import date


def date_now(request):
    return HttpResponse(f'{date.today()}')


def two_pow(request, number):
    assert isinstance(number, int)
    return HttpResponse(f'{2 ** number}')
