from django.urls import path
from  . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts1/', views.contacts, name='contacts',),
]