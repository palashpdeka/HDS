from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('items',views.items,name="items"),
path('add',views.add,name="add"),
 ]