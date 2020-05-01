from django.urls import path, include
from taskmanager import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
]
