from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import ToDo

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

