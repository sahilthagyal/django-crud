# Generated by Django 5.1.5 on 2025-02-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudmainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('pass1', models.CharField(max_length=50)),
                ('pass2', models.CharField(max_length=50)),
            ],
        ),
    ]
