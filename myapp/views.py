from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    print("control cam to views.py")
    return HttpResponse("<h1>Welcome to Pyspiders</h1>")#html tag

def home(request):
    return HttpResponse("<h1>Welcome to Homepage</h1>")