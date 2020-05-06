from django import forms
from django.contrib.auth.models import User

from taskmanager.models import Project, Status


class SearchProfileForm(forms.Form):
    projectname = forms.CharField(max_length=100)
    users = forms.CharField(max_length=100)


class TaskForm(forms.Form):

    # Defining fields to be expected in POST request
    project_id = forms.IntegerField()
    name = forms.CharField(max_length=80)
    description = forms.CharField(max_length=256)
    assignee_name = forms.CharField(max_length=80)
    start_date = forms.DateField()
    due_date = forms.DateField()
    priority = forms.IntegerField()
    status = forms.CharField(max_length=15)

    def clean(self):

        # Cleaning data before analyzing
        cleaned_data = super(TaskForm, self).clean()
        project_id = cleaned_data.get('project_id')
        assignee_name = cleaned_data.get('assignee_name')
        start_date = cleaned_data.get('start_date')
        due_date = cleaned_data.get('due_date')
        priority = cleaned_data.get('priority')
        status = cleaned_data.get('status')

        # Adding conditions and constraints
            # Checking if we are adding the task in an available project
        if not (Project.objects.filter(id=project_id).exists()):
            self.add_error("project_name", "This project name does not exist")

            # Checking if assignee is indeed in the user database
        if not (User.objects.filter(username=assignee_name)):
            self.add_error("Assignee username does not exist")

            # Just added for proper scaling
        if (priority < 0) or (priority > 10):
            self.add_error("priority", "Priority between 0 and 10!")

            # Due date cannot be before start date
        if due_date < start_date:
            self.add_error("due_date", "Due date should be bigger than start date")

            # Checking if the selected status is available in the database
        if not (Status.objects.filter(name=status)):
            self.add_error("status", "Status is not valid")

        return cleaned_data
