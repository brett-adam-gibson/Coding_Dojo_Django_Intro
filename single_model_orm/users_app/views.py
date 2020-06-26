
from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    return render(request, 'index.html')

def add_new_user(request):
    if request.method == 'POST':
        context = {
            'first_name': User.first_name()
            
        }