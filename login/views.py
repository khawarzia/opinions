from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import infor

def login(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    template = 'login.html'
    if request.method == 'POST':
        a = authenticate(username = request.POST['username'],password = request.POST['password'])
        print (a)
        if a is not None:
            auth.login(request,a)
            return redirect('/profile')
        else:
            return redirect('/login')
    return render(request,template)

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    template = 'signup.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            age = request.POST['age']
        except:
            age = 0
        obj = User.objects.create_user(
            username = username,
            password = password
        )
        obj.save()
        inforobj = infor()
        inforobj.user = obj
        inforobj.age = age
        inforobj.save()
        auth.login(request,obj)
        return redirect('/profile')
    return render(request,template)