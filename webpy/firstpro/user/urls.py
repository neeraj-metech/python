from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('', views.index, name="userhome"),
    path('about', views.about, name="userabout"),
]
