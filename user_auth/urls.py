from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('sign',views.sign,name="sign"),
    path('log',views.log,name="log"),
    path('logout',views.logoutUser,name="logout"),
]