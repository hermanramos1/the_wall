from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, "main_app/index.html")

def register(request): 

    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        if request.method == "POST":
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed_pw)
            request.session['user_id'] = new_user.id
            context = {
                'first_name' : new_user.first_name
            }
            return redirect("/wall")
         

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        if request.method == "POST":
            matching_users = User.objects.filter(email = request.POST['email'])
            if matching_users:
                user = matching_users[0]
            else:
                messages.error(request, "Incorrect Email")
                return redirect('/')
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/wall')
            else:
                messages.error(request, "Incorrect password")
                return redirect('/')



    