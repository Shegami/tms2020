from django.shortcuts import render, redirect
import requests
from catdog.models import AnimalImage
from datetime import datetime


def catdog(request):
    if request.method == 'GET':
        return render(request, 'catdog.html')
    else:
        if 'cat' in request.POST:
            return redirect('cat')
        else:
            return redirect('dog')


def cat(request):
    data = requests.get('https://aws.random.cat/meow').json()
    context = {
        'url': data['file']
    }
    if request.method == 'GET':
        return render(request, 'cat.html', context)
    else:
        if request.POST.get('button') == 'save':
            typpe = context['url'].split('.')[-1]
            save_model(context['url'], typpe).save()
        return redirect(catdog)


def dog(request):
    data = requests.get('https://dog.ceo/api/breeds/image/random').json()
    context = {
        'url': data['message']
    }
    if request.method == 'GET':
        return render(request, 'dog.html', context)
    else:
        if request.POST.get('button') == 'save':
            typpe = context['url'].split('.')[-1]
            save_model(context['url'], typpe).save()
        return redirect(catdog)


def save_model(url, typpe):
    model = AnimalImage(
                url=url,
                species='dog',
                date=datetime.now(),
                type=typpe
            )
    return model
