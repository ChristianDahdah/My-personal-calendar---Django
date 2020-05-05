from django.urls import path, include
from taskmanager import views

urlpatterns = [
    path('projects', views.projects),
    path('newproject', views.new_project),
    path('searchprofile', views.search_profile),

    # <int:id> is the project id
    path('projects/<int:id>', views.view_project),

    # <int:id> is the task id
    path('task/<int:id>', views.task),

]
