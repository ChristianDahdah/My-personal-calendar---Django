from django.urls import path, include
from accounts import views

urlpatterns = [
    path('profile/', views.profile),
    path('signup/', views.signup, name='signup'),

    # including the below path for easy authentication handling
    path('', include('django.contrib.auth.urls')),
]
