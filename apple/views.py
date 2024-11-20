from django.shortcuts import render
from django.http import HttpResponse

def myfunc(request):
    return HttpResponse("Hi my name is Pratik")
