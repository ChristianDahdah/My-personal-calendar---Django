from django import forms
from django.contrib.auth.models import User

from taskmanager.models import Project, Status


class SearchProfileForm(forms.Form):
    projectname = forms.CharField(max_length=100)
    users = forms.CharField(max_length=100)


class TaskForm(forms.Form):
    project_id = forms.IntegerField()
    name = forms.CharField(max_length=80)
    description = forms.CharField(max_length=256)
    assignee_name = forms.CharField(max_length=80)
    start_date = forms.DateField()
    due_date = forms.DateField()
    priority = forms.IntegerField()
    status = forms.CharField(max_length=15)

    def clean(self):

        print(self)
        cleaned_data = super(TaskForm, self).clean()
        print(cleaned_data)
        project_id = cleaned_data.get('project_id')
        assignee_name = cleaned_data.get('assignee_name')
        start_date = cleaned_data.get('start_date')
        due_date = cleaned_data.get('due_date')
        priority = cleaned_data.get('priority')
        status = cleaned_data.get('status')

        # Adding conditions
        if not (Project.objects.filter(id=project_id).exists()):
            self.add_error("project_name", "This project name does not exist")
        if not (User.objects.filter(username=assignee_name)):
            self.add_error("Assignee username does not exist")
        if (priority < 0) or (priority > 10):
            self.add_error("priority", "Priority between 0 and 10!")
        if due_date < start_date:
            self.add_error("due_date", "Due date should be bigger than start date")
        if not (Status.objects.filter(name=status)):
            self.add_error("status", "Status is not valid")

        return cleaned_data
