from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
# Create your models here.


class Note(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    title   = models.CharField(max_length=100)
    slug    = models.SlugField(blank=True, null=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(blank= True, default =datetime.datetime.now)
    active  = models.BooleanField(default=True)
    tags    = models.CharField(blank = True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug =slugify(self.title)
        super(Note,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes' 

