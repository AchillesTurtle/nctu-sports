from django import forms
from .models import Announcement

class AnncForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'text', 'picture')