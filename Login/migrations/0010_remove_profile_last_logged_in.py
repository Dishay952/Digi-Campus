# Generated by Django 4.0.3 on 2022-03-31 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0009_alter_profile_last_logged_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_logged_in',
        ),
    ]
