from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdinm(admin.ModelAdmin):
    list_display = ['user','slug','headline','join']
    list_filter = ['headline','join']
    search_fields =['user__first_name'] # because user is forn key  and relation 
    list_editable = ['slug']







#user
#slug
#headline
#bio
#join
admin.site.register(Profile,ProfileAdinm)