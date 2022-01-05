from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib import messages
# Create your views here.

def home(request):
    HttpResponse('Hello, I\'m working')
    return render(request, 'login/index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['PASS1']
        pass2 = request.POST['PASS2']

        myuser = User.objects.create(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, 'Account created successfully!')

        return redirect('signin')

    return render(request, 'login/signup.html')


def signin(request):
    return render(request, 'login/signin.html')


def signout(request):
    return render(request, 'login/signout.html')
