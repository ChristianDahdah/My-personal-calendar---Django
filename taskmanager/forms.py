from django import forms


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=100)
    members = forms.IntegerField(blank=False)


class SearchProfileForm(forms.Form):
    profiles = forms.ModelMultipleChoiceField()