from django.urls import path

# importing views from views.py
from .views import *
from .views import home_view

urlpatterns = [
    path('',home_view, name='home'),
]
