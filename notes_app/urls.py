from . import views
from django.urls import path

app_name='notes_app'
urlpatterns = [
    path('',views.all_notes,name='all_notes'),
    path('detail/<slug:slug>/',views.detail,name='detail'),
    path('add/',views.not_add,name='not_add'),
]