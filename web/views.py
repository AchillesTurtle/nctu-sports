from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from .models import Announcement

def home(request):
    anncs = Announcement.objects.all().order_by('-published_date')
    return render(request,'web/home.html',{'anncs':anncs})

def anncdetail(request, pk):
    annc = Announcement.objects.get(pk=pk)
    return render(request,'web/anncs.html',{'annc':annc})

@permission_required('Announcement.delete', login_url='login')
def anncdelete(request, pk):
    anncs = Announcement.objects.get(pk=pk)
    return render(request,'web/home.html',{'anncs':anncs})

@permission_required('Announcement.add', login_url='login')
def anncadd(request):
    annc = Announcement.objects.get(pk=pk)
    return render(request,'web/anncs.html',{'annc':annc})

@permission_required('Announcement.change', login_url='login')
def anncedit(request, pk):
    annc = Announcement.objects.get(pk=pk)
    return render(request,'web/anncs.html',{'annc':annc})