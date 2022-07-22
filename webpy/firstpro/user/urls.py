from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('', views.index, name="userhome"),
    path('allusers', views.allusers, name="allusers"),
    path('edit/<id>', views.editUser, name="editUser"),
]
