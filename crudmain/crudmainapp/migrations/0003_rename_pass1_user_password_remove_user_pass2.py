# Generated by Django 5.1.5 on 2025-02-02 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudmainapp', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pass1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pass2',
        ),
    ]
