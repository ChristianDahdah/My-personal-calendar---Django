from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('accounts.Profile')

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='task_project')
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=256)
    assignee = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='task_assignee')
    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)
    priority = models.PositiveSmallIntegerField(default=0)
    status = models.ForeignKey("Status", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Journal(models.Model):
    date = models.DateTimeField(default=timezone.now)
    entry = models.CharField(max_length=256)
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)

    def __str__(self):
        return "Journal fait par {} pour la tâche '{}'".format(self.author, self.task.name)
