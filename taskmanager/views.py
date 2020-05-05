from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf

from taskmanager.forms import SearchProfileForm
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
    #profle passed as a parameter to put profile picture and first name in the website's header
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = SearchProfileForm(request.POST)
        if form.is_valid():
            print(form)
            projectname = form.cleaned_data["projectname"]
            users = form.cleaned_data["users"]


    return render(request, 'taskmanager/newproject.html', locals())


@login_required
def search_profile(request):
    if request.method == "POST":
        search_profile = request.POST['search_profile']
    else:
        search_profile = ''

    profiles = Profile.objects.filter(user__username__contains=search_profile)

    return render_to_response('taskmanager/searchprofile.html', locals())

