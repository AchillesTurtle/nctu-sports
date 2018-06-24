from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(blank=True,null=True,upload_to='static/anncpic/')

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class SportsEvent(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateField()
    team_limit = models.IntegerField()
    size_limit = models.IntegerField()
    is_deleted = models.BooleanField (default=False)
    picture = models.ImageField(blank=True,null=True,upload_to='static/eventspic/')

    reg_teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name
    
    @property
    def is_past_due(self):
        return date.today() > self.start_date   