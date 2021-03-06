from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import date


def date_now(request):
    return HttpResponse(f'{date.today()}')


def two_pow(request, number):
    assert isinstance(number, int)
    return HttpResponse(f'{2 ** number}')


def my_word(request, word):
    if len(word) % 2 == 0:
        return HttpResponse(f'{word[1::2]}')
    else:
        redirect('main')
