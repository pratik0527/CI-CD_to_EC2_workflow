from django.shortcuts import render
from django.http import HttpResponse

def myfunc(request):
    return HttpResponse("my name is Pratik")