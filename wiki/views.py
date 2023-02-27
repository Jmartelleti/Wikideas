from .models import wiki
from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

