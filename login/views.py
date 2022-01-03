from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    HttpResponse('Hello, I\'m working')
    return render(request, 'login/index.html')

def signup(request):
    return render(request, 'login/signup.html')

def signin(request):
    return render(request, 'login/signin.html')

def signout(request):
    return render(request, 'login/signout.html')