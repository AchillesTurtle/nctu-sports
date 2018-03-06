from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'index.html')

