from django.contrib import admin
from .models import Note

 ## to filter my notes in my admin panal
class NotesAdmin(admin.ModelAdmin):   
    list_filter = ['active','created']
    list_display =['title','created','active']
    search_fields = ['title','content']


#this tages from models we can uses in filte 

#user
#title
#slug
#content
#created
#active
#tags



admin.site.register(Note,NotesAdmin)