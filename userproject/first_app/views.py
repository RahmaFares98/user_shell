from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .models import User 

def users_list(request):
    users = User.objects.all()
    #del_user = User.objects.get(id=1)	
    # del_user.delete()
    return render(request, 'users.html', {'users': users})

def add_user(request):
    if request.method == 'POST': ## if method equal post take the data from form and save it in variable
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        User.create_user(first_name=first_name, last_name=last_name, email=email, age=age)
        return redirect('/')
    return HttpResponse("invalid rotation")