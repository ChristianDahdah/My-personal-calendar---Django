from django.urls import path, include
from accounts import views

urlpatterns = [
    path('profile/', views.profile),
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
]
