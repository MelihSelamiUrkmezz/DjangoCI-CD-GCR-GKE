from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Will be soon!")

def blogs(request):
    return HttpResponse("Will be soon blogs!")