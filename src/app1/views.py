from django.http import HttpResponse
from datetime import date


def date_now(request):
    return HttpResponse(f'{date.today()}')
