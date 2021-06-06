from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from shopping.models import order,product,customer

@login_required(login_url='log')
def items(request):
    pr=product.objects.all()
    return render(request,'item.html',{'product':pr})

@login_required(login_url='log')
def add(request):
    if request.method=='POST':
        pro=request.POST['name'] #pro=product
        qnt=request.POST['quantity']
        prc=product.objects.get(name=pro)
        p=prc.price
        new=order.objects.create(user=request.user, item=pro, quantity=qnt, price=qnt*p)
        #new.status=0 #0-on bag, 1-ordered, 2-out for delivery, 3-delivered, 4-cancelled
        new.save()
        return redirect('shopping/items')
    else:
        return redirect('shopping/items')
