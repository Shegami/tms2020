from django.shortcuts import render, redirect


def catdog(request):
    if request.method == 'GET':
        return render(request, 'catdog')
