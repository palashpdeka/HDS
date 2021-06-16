from django.contrib import admin
from .models import product,order,customer

admin.site.register(product)
admin.site.register(order)
admin.site.register(customer)