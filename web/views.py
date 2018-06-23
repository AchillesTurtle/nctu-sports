from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from .models import Announcement

def home(request):
    anncs = Announcement.objects.all().order_by('-published_date')
    return render(request,'web/home.html',{'anncs':anncs})

def anncdetail(request, pk):
    annc = get_object_or_404(Announcement, pk=pk)
    return render(request,'web/anncs.html',{'annc':annc})

@permission_required('Announcement.delete', login_url='login')
def anncdelete(request, pk):
    Announcement.objects.filter(pk=pk).delete()
    return redirect('home')

@permission_required('Announcement.add', login_url='login')
def anncadd(request):
    annc = Announcement.objects.get(pk=pk)
    return render(request,'web/anncs.html',{'annc':annc})

@permission_required('Announcement.change', login_url='login')
def anncedit(request, pk):
    annc = Announcement.objects.get(pk=pk)
    return render(request,'web/anncs.html',{'annc':annc})