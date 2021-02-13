from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import UserForm

# Create your views here.

def index(request):
    data_dict = {'insertme': 'WELCOME TO HOME PAGE'}
    return render(request,'first_app/index.html',context=data_dict)

def home(request):
    userform = UserForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            # im starting index in the same path as userform/
            return index(request)
    return render(request,'first_app/userform.html',context={'userform':userform})