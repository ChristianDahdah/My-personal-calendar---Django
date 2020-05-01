from django import forms
# from django.core.validators import MinLengthValidator


class ProfileForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=60, required=True)
    # Last_name isn't required
    last_name = forms.CharField(label="Nom", max_length=60, required=False)

    # username, password AND email are required to successfully create a user from User model
    # A first name field was also added just to say Welcome "First name" in login page
    username = forms.CharField(label="Nom d'utilisateur", max_length=80, required=True)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, required=True)
    email = forms.CharField(label="Adresse email", widget=forms.EmailInput, required=True)

    # add groups and avatar later
