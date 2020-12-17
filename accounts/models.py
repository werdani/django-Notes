from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    slug       = models.SlugField(blank=True, null=True)
    headline   = models.CharField(max_length=50)
    bio        = models.TextField(max_length=500)
    image      = models.ImageField(upload_to='profile_img')
    join       = models.DateTimeField(default=datetime.datetime.now)
    


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug =slugify(self.first_name)
        super(Profile,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.user)

## signals   >> when action crate thing .
# when create user create profile. 
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)