from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Announcement, SportsEvent, Team
from .forms import AnncForm, EventForm, TeamForm

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
    messages.success(request, '刪除成功！')
    return redirect('home')

# Events part:
def eventlist(request):
    events = SportsEvent.objects.filter(is_deleted=False).order_by('-start_date')
    return render(request,'web/events.html', {'events':events})

@login_required
def eventsignup(request, pk):
    event = get_object_or_404(SportsEvent.objects.filter(is_deleted=False), pk=pk)    
    if request.method == 'POST':
        # check team limit
        if request.user.is_authenticated and request.user.has_perm('SportsEvent.change'):
            form = TeamForm(request.POST)            
            if form.is_valid():                
                team = form.save()
                event.reg_teams.add(team)
                event.save()
                messages.success(request, '報名成功！')
                return redirect('eventlist')
        else:
            if event.team_limit <= event.reg_teams.count():
                messages.error(request, '隊伍數已滿！')
                return redirect('eventlist')
            else:
                form = TeamForm(request.POST)            
                if form.is_valid():                
                    team = form.save(commit=False)
                    if event.size_limit < form.cleaned_data.get('students').count():
                        messages.error(request, '超過規定人數！')
                        return render(request,'web/events_signup.html', {'event':event, 'form':form})
                    else:
                        team.save()
                        form.save_m2m()
                        event.reg_teams.add(team)
                        event.save()
                        messages.success(request, '報名成功！')
                    return redirect('eventlist')
    else:
        form = TeamForm()
    return render(request,'web/events_signup.html', {'event':event, 'form':form})

@login_required
def eventsignup_edit(request, pk):
    # check if self included
    team = get_object_or_404(Team, pk=pk)
    if request.user not in team.students.all() and not request.user.has_perm('SportsEvent.change'):
        return redirect('eventsignup_list')
    event = get_object_or_404(SportsEvent.objects.filter(is_deleted=False), reg_teams=team)    
    if request.method == 'POST':
        form = TeamForm(request.POST or None, instance=team)  
        if request.user.is_authenticated and request.user.has_perm('SportsEvent.change'):         
            if form.is_valid():                
                team = form.save()
                messages.success(request, '修改成功！')
                return redirect('eventsignup_list')
        else:                      
            if form.is_valid():                
                team = form.save(commit=False)
                if event.size_limit < form.cleaned_data.get('students').count():
                    messages.error(request, '超過規定人數！')
                    return render(request,'web/events_signup_edit.html', {'event':event, 'form':form})
                else:
                    team.save()
                    form.save_m2m()
                    messages.success(request, '修改成功！')
                return redirect('eventsignup_list')
    else:
        form = TeamForm(instance=team)
    return render(request,'web/events_signup_edit.html', {'event':event, 'form':form})

@login_required
def eventsignup_list(request):
    result = []
    if request.user.has_perm('SportsEvent.change'):
        myteams = Team.objects.all()
    else:
        myteams = Team.objects.filter(students=request.user).all()
    for event in SportsEvent.objects.all():
        temp=(event,[])
        for team in myteams:
            if team in event.reg_teams.all():
                temp[1].append(team)
        if len(temp[1]):
            result.append(temp)
    result=sorted(result, key=lambda x: x[0].name)
    return render(request,'web/events_signup_list.html', {'result':result})

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
    messages.success(request, '刪除成功！')
    return redirect('eventlist')