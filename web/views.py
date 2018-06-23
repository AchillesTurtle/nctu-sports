from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from .models import Announcement
from .forms import AnncForm

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
    if request.method == 'POST':
        form = AnncForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnncForm()
    return render(request,'web/anncs_add.html',{'form': form})

@permission_required('Announcement.change', login_url='login')
def anncedit(request, pk):
    annc = Announcement.objects.get(pk=pk)
    if request.method == 'POST':
        form = AnncForm(request.POST or None, request.FILES, instance=annc)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnncForm()
    return render(request,'web/anncs_edit.html',{'form':form, 'annc':annc})