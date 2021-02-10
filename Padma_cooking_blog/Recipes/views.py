from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "welcome/hello.html")

def swa(request):
    return HttpResponse("Hi Swa!")

def amb(request):
    return HttpResponse("Hi AMB!")

def greet(request, name):
    return render(request, "welcome/greet.html", {
        "name": name.capitalize()
    })