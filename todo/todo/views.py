from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import ToDo
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def signup(request):

    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        print(fnm, emailid, pwd)
        new_user = User.objects.create_user(fnm, emailid, pwd)
        new_user.save()
        return redirect('/login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)
        auth_user = authenticate(username=fnm, password=pwd)
        if auth_user is not None:
            auth_login(request, auth_user)
            return redirect('/todo')
    return render(request, 'login.html')

def todo(request):
    return render(request, 'todo.html')