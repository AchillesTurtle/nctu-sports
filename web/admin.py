from django.contrib import admin
from .models import Announcement, SportsEvent, Team
# Register your models here.

admin.site.register(Announcement)
admin.site.register(SportsEvent)
admin.site.register(Team)