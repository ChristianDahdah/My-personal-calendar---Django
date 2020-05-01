from django import forms
from django.core.validators import MinLengthValidator


class ProfilForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=60)
    # Last_name isn't required
    last_name = forms.CharField(label="Nom", max_length=60, required=False)
    username = forms.CharField(label="Nom d'utilisateur", max_length=80)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    email = forms.CharField(label="Adresse email", widget=forms.EmailInput)

    #add groups and avatar later





