from django import forms
from .models import Announcement, SportsEvent

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