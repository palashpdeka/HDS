from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import order,product,customer
from .decorators import unauth_user,allowed_user

@login_required(login_url='log')
def items(request):
    pr=product.objects.all()
    return render(request,'item.html',{'product':pr})

@login_required(login_url='log')
def add(request):
    if request.method=='POST':
        pro=request.POST['name'] #pro=product
        qnt=request.POST['quantity']
        q=int(qnt)
        prc=product.objects.get(name=pro)
        p=prc.price
        new=order.objects.create(user=request.user.username, name=pro, quantity=qnt, price=q*p)
        #0-on bag, 1-ordered, 2-out for delivery, 3-delivered, 4-cancelled, 5-removed_from_bag, 6-not-available
        new.save()
        return redirect('items')
    else:
        return redirect('items')

@login_required(login_url='log')
def bag(request):
     user=request.user.username
     cus=customer.objects.get(user=user)
     orders=order.objects.filter(user=user,status=0)
     return render(request,'bag.html',{'customer':cus,'orders': orders})

@login_required(login_url='log')
def remove(request):
    if request.method=='POST':
        idd=request.POST['id']
        ord=order.objects.get(id=int(idd))
        ord.status=5
        ord.save()
        return redirect('bag')
    else:
        return redirect('bag')

@login_required(login_url='log')
def order_all(request):
    if request.method == 'POST':
        orders=order.objects.filter(user=request.user.username, status=0)
        for ord in orders:
            ord.status=1
            ord.save()
        return redirect('bag')
    else:
        return redirect('bag')

@login_required(login_url='log')
@allowed_user(allowed_roles=['Delivery_Man'])
def seeOrders(request):
     orders=order.objects.filter(status=1)
     users=set()
     for oord in orders:
         users.add(oord.user)
     return render(request,'seeOrders.html',{'users':users})

@login_required(login_url='log')
@allowed_user(allowed_roles=['Delivery_Man'])
def chkOrdUser(request):
    if request.method=='POST':
        usr=request.POST['usrname']
        return chkOrdUser2(request,usr)
    else:
        return redirect('seeOrders')


@login_required(login_url='log')
@allowed_user(allowed_roles=['Delivery_Man'])
def chkOrdUser2(request,usr):
        cus=customer.objects.get(user=usr)
        ordr=order.objects.filter(user=usr,status=1)
        return render(request,'seeOrders.html',{'cust':cus,'order':ordr})

def availability(request):
    if request.method=='POST':
        idd=int(request.POST['id'])
        ord=order.objects.get(id=idd)
        ord.status=8
        usr=ord.user
        ord.save()
        return chkOrdUser2(request,usr)
    else:
        return redirect ('seeOrders')