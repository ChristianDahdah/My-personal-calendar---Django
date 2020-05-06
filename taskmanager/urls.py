from django.urls import path, include
from taskmanager import views

urlpatterns = [
    path('projects', views.projects),
    path('newproject', views.newproject),
    path('searchprofile', views.searchprofile),

    # <int:id> is the project id
    path('projects/<int:id>', views.viewproject),

    # <int:id> is the task id
    path('task/<int:id>', views.task),

    # <int:id> is the project id
    path('newtask/<int:id>', views.newtask),

    # this path is used to search for users when creating/editing a task
    path('searchassignee', views.searchassignee),

    # <int:id> is the task id
    path('edittask/<int:id>', views.edittask),
]
