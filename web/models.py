from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(blank=True,null=True,upload_to='static/anncpic/')

    def __str__(self):
        return self.title