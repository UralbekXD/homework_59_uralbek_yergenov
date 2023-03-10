# Generated by Django 4.1.6 on 2023-03-10 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0004_alter_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='issue_tracker.project', verbose_name='Проект'),
        ),
    ]
