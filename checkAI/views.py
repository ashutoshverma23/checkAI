from django.http import HttpRequest
from django.shortcuts import render

def aboutUS(request):
    return HttpRequest("Welcome to checkAI")

def homePage(request):
    return render(request, 'index.html')
