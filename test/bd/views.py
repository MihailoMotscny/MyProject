from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Artiles
from .forms import LoginForm
from .forms import ArticlesForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import RegisterForm

def home_prices(request):
    prices=Artiles.objects.all()
    return render(request, 'bd/prices.html',{'prices':prices})

def profil(request):
    return render(request, 'bd/profil.html',{'profil':profil})



def create(request):
    error = ''
    idUser=0
    if request.method == 'POST':
        form=ArticlesForm(request.POST)
        if form.is_valid():
            idUser=request.user.id
            form.save()
        else:
            error = 'Заповніть всі поля'

    form = ArticlesForm()
    data={
        'form':form,
        'idUser':idUser,
        'error':error,

    }

    return render(request, 'bd/create.html',data)


def register(response):
    error = ''
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():

            form.save()
            return redirect('home')
        else:
            error="Спробуйте ще раз"

    else:
        form = UserCreationForm()
    data = {
        'form': form,
        'error': error,

    }

    return render(response, 'bd/register.html', data)



def logi(request):
    error=''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login( request,user)
                    return redirect("profil")
                else:
                    error='Обліковий запис не знайдено'
            else:
                error='Неправильний логін або пароль'
    else:
        form = LoginForm()

    data = {
        'form': form,
        'error': error,

    }

    return render(request, 'bd/login.html', data)




# def idUser(request):
#     return request.user.id
