from django.shortcuts import render, redirect
import requests


def catdog(request):
    if request.method == 'GET':
        return render(request, 'catdog.html')
    else:
        if 'cat' in request.POST:
            return redirect('cat')
        else:
            return redirect('dog')


def cat(request):
    if request.method == 'GET':
        data = requests.get('https://aws.random.cat/meow').json()
        context = {
            'link': data['file']
        }
        return render(request, 'cat.html', context)
    else:
        return redirect(catdog)


def dog(request):
    if request.method == 'GET':
        data = requests.get('https://dog.ceo/api/breeds/image/random').json()
        context = {
            'link': data['message']
        }
        return render(request, 'dog.html', context)
    else:
        return redirect(catdog)
