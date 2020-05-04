from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf

from taskmanager.models import Project
from accounts.models import Profile


@login_required
def projects(request):
    if request.user.is_authenticated:
        # if a user is logged in then he can see his projects
        # Fetching profile to put it as an argument when rendering page
        profile = Profile.objects.get(user=request.user)
        projects = Project.objects.filter(members=profile)

    return render(request, 'taskmanager/projects.html', locals())


@login_required
def newproject(request):
    args = {}
    args.update(csrf(request))
    profile = Profile.objects.get(user=request.user)
    return render(request, 'taskmanager/newproject.html', locals())


@login_required
def searchprofile(request):
    print("I am in views.searchprofile")
    if request.method == "POST":
        search_profile = request.POST['search_profile']
    else:
        search_profile = ''

    profiles = Profile.objects.filter(user__username__contains=search_profile)

    return render_to_response('taskmanager/searchprofile.html', locals())
