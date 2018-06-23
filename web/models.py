from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(blank=True,null=True)
    picname = models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return self.title