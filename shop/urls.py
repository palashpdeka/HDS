from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('items',views.items,name="items"),
path('add',views.add,name="add"),
path('seeOrders',views.seeOrders,name="seeOrders"),
path('bag',views.bag,name="bag"),
path('remove',views.remove,name="remove"),
path('order_all',views.order_all,name="order_all"),
path('chkOrdUser',views.chkOrdUser,name="chkOrdUser"),
path('availability', views.availability, name="availability"),
 ]