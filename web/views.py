from django.http import HttpResponse

from django.shortcuts import render

def hello(request):
    return HttpResponse("<h3>Hello, World!</h3>")


def about(request):
    return HttpResponse("About us")
