from django.contrib.auth.models import User
from django.shortcuts import render
from taskmanager.forms import ProfilForm
from taskmanager.models import Profil


# Create your views here.


def signup(request):
    # Getting Post HTTP request
    form = ProfilForm(request.POST or None)

    if form.is_valid():

        # Creating a new User to put it as an attribute when creating a new Profile
        user = User()
        user.username = form.cleaned_data['username']
        user.password = form.cleaned_data['password']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()

        # Saving new created profile
        Profil(user=user).save()

        # Parameter used in singup.html to indicate that the profil was succesfully created
        envoi = True

    return render(request, 'taskmanager/signup.html', locals())

    return render(request, 'taskmanager/signup.html', locals())
