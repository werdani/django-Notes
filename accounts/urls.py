from . import views
from django.urls import path 
from django.contrib.auth import logout 
app_name='accounts'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',logout),
    path('signup/',views.signup,name='signup'),
    path('change_password/',views.change_pass,name='change_pass'),
    path('profile/<slug:slug>/',views.profile,name='profile'),
    path('profile/<slug:slug>/edit/',views.edit_profile,name='edit'),

]