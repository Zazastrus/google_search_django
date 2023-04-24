from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "search/index.html")

def image(request):
    return render(request, "search/image.html")

def advanced(request):
    return render(request, "search/advanced.html")