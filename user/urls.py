from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),
    path("get-users", views.getUsers, name='getUsers')
]
