from django.urls import path, include
from taskmanager import views

urlpatterns = [
    path('projects', views.projects),
    path('newproject', views.newproject),
    path('searchprofile', views.searchprofile),
]
