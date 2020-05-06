from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, render, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf

from taskmanager.forms import SearchProfileForm, TaskForm
from taskmanager.models import Project, Task, Journal, Status
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
    # profle passed as a parameter to put profile picture and first name in the website's header
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = SearchProfileForm(request.POST)
        if form.is_valid():
            projectname = form.cleaned_data["projectname"]
            users = form.cleaned_data["users"]

    return render(request, 'taskmanager/newproject.html', locals())


@login_required
def searchprofile(request):
    if request.method == "POST":
        search_profile = request.POST['search_profile']
    else:
        search_profile = ''

    profiles = Profile.objects.filter(user__username__contains=search_profile)

    return render_to_response('taskmanager/searchprofile.html', locals())


@login_required
def viewproject(request, id):
    # Needed to load avatar in upper page
    profile = Profile.objects.get(user=request.user)

    # Checking if the project with the requested id exists
    try:
        project = Project.objects.get(id=id)
        tasks = Task.objects.filter(project__id=id)
    except Project.DoesNotExist:
        raise Http404

    return render(request, 'taskmanager/view_project.html', locals())


@login_required
def task(request, id):
    # Needed to load avatar in upper page
    profile = Profile.objects.get(user=request.user)

    try:
        task = Task.objects.get(id=id)
        journals = Journal.objects.filter(task__id=id)
    except Project.DoesNotExist:
        raise Http404

    return render(request, 'taskmanager/task.html', locals())


@login_required
def newtask(request, id):
    # Needed to load avatar in upper page
    profile = Profile.objects.get(user=request.user)

    # Checking if the project with the current id exists
    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        raise Http404

    if request.method == "POST":
        print(request.POST)
        form = TaskForm(request.POST)
        print(form)

        if form.is_valid():
            # getting cleaned data
            print("THE FORM IS VALID")

            project_id = form.cleaned_data['project_id']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            assignee_name = form.cleaned_data['assignee_name']
            start_date = form.cleaned_data['start_date']
            due_date = form.cleaned_data['due_date']
            priority = form.cleaned_data['priority']
            status = form.cleaned_data['status']

            # injecting data
            task = Task()
            task.project = Project.objects.get(id=id)
            task.name = name
            task.description = description
            task.assignee = Profile.objects.get(user__username=assignee_name)
            task.start_date = start_date
            task.due_date = due_date
            task.priority = priority
            task.status = Status.objects.get(name=status)

            # Saving info
            task.save()

            return redirect('/taskmanager/task/'+str(task.id))

    return render(request, 'taskmanager/newtask.html', locals())



@login_required
def searchassignee(request):
    if request.method == "POST":
        search_assignee = request.POST['search_assignee']
    else:
        search_assignee = ''

    profiles = Profile.objects.filter(user__username__contains=search_assignee)

    return render_to_response('taskmanager/searchassignee.html', locals())
