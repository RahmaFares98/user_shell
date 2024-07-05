from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .models import User ,create_user

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
        create_user(first_name,last_name,email,age)#call create user 
        return redirect('/')
    return HttpResponse("Invalid request method.", status=400)# if there is error return this 
