from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Announcement, SportsEvent
from .forms import AnncForm, EventForm

def home(request):
    anncs = Announcement.objects.all().order_by('-published_date')
    return render(request,'web/home.html',{'anncs':anncs})

# Anncs part:
def anncdetail(request, pk):
    annc = get_object_or_404(Announcement, pk=pk)
    return render(request,'web/anncs.html',{'annc':annc})

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

@permission_required('Announcement.delete', login_url='login')
def anncdelete(request, pk):
    Announcement.objects.filter(pk=pk).delete()
    messages.success(request, '刪除成功!')
    return redirect('home')

# Events part:
def eventlist(request):
    events = SportsEvent.objects.filter(is_deleted=False).order_by('-start_date')
    return render(request,'web/events.html', {'events':events})

def eventsignup(request, pk):
    events = SportsEvent.objects.all().order_by('-start_date')
    return render(request,'web/events.html', {'events':events})

@permission_required('SportsEvent.change', login_url='login')
def eventstatus(request, pk):
    event = get_object_or_404(SportsEvent, pk=pk)
    return render(request,'web/event_status.html',{'event':event})

@permission_required('SportsEvent.add', login_url='login')
def eventadd(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('eventlist')
    else:
        form = EventForm()
    return render(request,'web/events_add.html',{'form': form})

@permission_required('SportsEvent.change', login_url='login')
def eventedit(request, pk):
    event = SportsEvent.objects.get(pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST or None, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('eventlist')
    else:
        form = EventForm()
    return render(request,'web/events_edit.html',{'form':form, 'event':event})

@permission_required('SportsEvent.delete', login_url='login')
def eventdelete(request, pk):
    event = SportsEvent.objects.get(pk=pk)
    event.is_deleted = True
    event.save()
    messages.success(request, '刪除成功!')
    return redirect('eventlist')