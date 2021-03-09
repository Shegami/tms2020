from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import date
from django.template.loader import get_template


def date_now(request):
    return HttpResponse(f'{date.today()}')


def two_pow(request, number):
    assert isinstance(number, int)
    return HttpResponse(f'{2 ** number}')


def my_word(request, word):
    if len(word) % 2 == 0:
        return HttpResponse(f'{word[1::2]}')
    else:
        return redirect('main')


def form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        with open('../src/app1/django_04.txt', 'w') as my_file:
            my_file.writelines([
                f'First name: {first_name}\n',
                f'Last name: {last_name}\n',
                f'Age: {age}\n',
                '\n'
            ])
            return redirect('form')
    else:
        template = get_template('django_04.html')
        response = template.render({}, request)
        return HttpResponse(response)


def full_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'age': age
        }
        return render(request, 'django_06_display.html', context)
    else:
        return render(request, 'django_06_form.html')
