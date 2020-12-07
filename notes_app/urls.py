from . import views
from django.urls import path

app_name='notes_app'
urlpatterns = [
    path('',views.all_notes,name='all_notes'),
    path('detail',views.detail,name='detail'),
]