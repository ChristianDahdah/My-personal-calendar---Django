# Generated by Django 2.1.15 on 2020-05-02 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0004_auto_20200502_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_project', to='taskmanager.Project'),
        ),
    ]
