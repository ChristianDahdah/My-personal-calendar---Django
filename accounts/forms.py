from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=60, required=True)
    last_name = forms.CharField(label="Nom", max_length=60, required=True)
    # username, password AND email are required to successfully create a user from User model
    # A first name field was also added just to say Welcome "First name Last Name" in login page
    username = forms.CharField(label="Nom d'utilisateur", max_length=80, required=True)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, required=True)
    email = forms.CharField(label="Adresse email", widget=forms.EmailInput, required=True)

    # Avatar isn't a required field because system will assign a default profile picture in case the user didn't
    avatar = forms.ImageField(label="Image de profil", required=False)