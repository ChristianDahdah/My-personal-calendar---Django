from django.urls import path
from taskmanager import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
]
