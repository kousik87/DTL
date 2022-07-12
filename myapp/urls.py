from turtle import home
from django.urls import path
from .views import *

urlpatterns = [
path('',home,name='home'),    
path('/contact',contact_us,name='contact'),    
]
