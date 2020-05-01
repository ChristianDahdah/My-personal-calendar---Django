from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from accounts.forms import ProfileForm
from accounts.models import Profile


@login_required
def profile(request):
    return render(request, 'profile.html')


def signup(request):
    # Getting Post HTTP request
    form = ProfileForm(request.POST or None)

    if form.is_valid():
        # Creating a new User to put it as an attribute when creating a new Profile
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        # User.objects.create_user creates a user and saves it automatically
        # username, password AND email are required to successfully create a user from User model
        # A first name field was also added just to say Welcome "First name" in login page
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)
        # Parameter used in singup.html to indicate that the profil was succesfully created

        # Creating and saving a profile
        profile = Profile.objects.create(user=user)
        envoi = True

    return render(request, 'accounts/signup.html', locals())