from django.contrib import admin
from django.urls import path
from . import views

app_name='userauths'
urlpatterns = [
    path('signup/',views.userregister,name='userregister'),
    path('signin/',views.userlogin,name='userlogin'),
    path('signout/',views.userlogout,name='userlogout'),
]