from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Hello fellow developers.</h>")

def contact_page(request):
    return HttpResponse("<h1>This is my contact page.</h1>")

def about_page(request):
    return HttpResponse("<h1>This is our my contact page.</h1>")



# Create your views here.
