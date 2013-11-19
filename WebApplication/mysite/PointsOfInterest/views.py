from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at our exciting site about Points of Interest")

# Create your views here.
