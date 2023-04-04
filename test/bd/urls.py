from django.urls import path
from  . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.home_prices, name='home_prices'),
    path('create', views.create, name='create'),
    path("register/", views.register, name="register"),
    path("profil/", views.profil, name="profil"),
    path("login/", views.logi, name="login"),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),

]