from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'homepage.html')

def sign(request):
    if request.method=='POST':
        global name
        global userid
        user=request.POST['username']
        #name=user
        first=request.POST['first']
        last=request.POST['last']
        phn=request.POST['phn']
        pw=request.POST['password']
        person=User.objects.create_user(username=user,first_name=first,last_name=last,password=pw)
        #group=Group.objects.get(name='Students')
        #person.groups.add(group)
        userid=person.id
        print('User Created')
        auth.login(request, person)
        return redirect('shopping/items')
    else:
        return render(request,"signup.html")

def log(request):
    if request.method=='POST':
        global name
        global userid
        user=request.POST['username']
        pw=request.POST['password']
        person=auth.authenticate(username=user,password=pw)
        userid=person.id
        if person is not None:
            auth.login(request,person)
            print('Login successfull')
            return redirect('shopping/items')
        else:
            print('Wrong username or password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

@login_required()
def logoutUser(request):
    logout(request)
    return redirect('/')
