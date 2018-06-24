from django import forms
from django.contrib.auth.models import User
from .models import Announcement, SportsEvent, Team

class AnncForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'text', 'picture')

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):
    class Meta:
        model = SportsEvent
        fields = ('name', 'start_date', 'team_limit', 'size_limit', 'text', 'picture', 'is_deleted')
        widgets = {
            'start_date': DateInput(),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'students')

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder' : '範例：老司機隊', 'class' : 'form-control'})
        self.fields['students'].widget.attrs.update({'class' : 'form-control'})

        self.fields['name'].label='隊伍名稱'
        self.fields['students'].label='隊伍成員 (按住ctrl鍵一次選取多名隊員)'
        self.fields['students'].queryset= User.objects.order_by('username')

        mychoices = []
        for userid, username in self.fields['students'].choices:
            tempuser = User.objects.get(username=username)
            mychoices.append((tempuser.id, username+" "+tempuser.last_name+tempuser.first_name))
        self.fields['students'].choices = mychoices