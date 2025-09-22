from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from todo import models
from todo.models import ToDo
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.ToDo(title=title, user=request.user)
        obj.save()
        user = request.user
        res = models.ToDo.objects.filter(user=request.user).order_by('-date')
        return render(request, 'todo.html', {'res': res})
    res = models.ToDo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html' , {'res': res})

@login_required(login_url='/login')
def edit_todo(request, sn):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.ToDo.objects.get(sn=sn)
        obj.title = title
        obj.save()
        return redirect('/todo')

    obj = models.ToDo.objects.get(sn=sn)
    return render(request, 'edit_todo.html', {'obj': obj})

@login_required(login_url='/login')
def delete_todo(request, sn):
    obj = models.ToDo.objects.get(sn=sn)
    obj.delete()
    return redirect('/todo')

def logout(request):
    auth_logout(request)
    return redirect('/login')
