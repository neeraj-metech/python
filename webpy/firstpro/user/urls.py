from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('', views.index, name="userhome"),
    path('allusers', views.allusers, name="allusers"),
    path('allposts', views.allposts, name="allposts"),
    path('allposts/<userId>', views.allposts, name="view_post"),
    path('edit/<id>', views.editUser, name="editUser"),
]
