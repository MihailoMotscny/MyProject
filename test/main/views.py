from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html', {'title':'Головна сторінка'})


def about(request):
    return render(request, 'main/test.html', {'title':'Про нас'})


def contacts(request):
    return render(request, 'main/testblock.html', {'title':'Підтримка'})
