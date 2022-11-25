from django.contrib.auth.models import User
from django.shortcuts import render

def register(request):
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password=password)
        user.save()
        print("user created")
    else:
        print("password not match")
    return render(request,'register.html')