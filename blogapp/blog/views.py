from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Je t'aime mon plus bel ange, ma rose!")

def blogs(request):
    return HttpResponse("Je vous aimerai pour toujours!")