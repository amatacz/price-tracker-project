# Generated by Django 4.1 on 2022-09-17 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricemonitor', '0003_userprofile_productuserrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.DeleteModel(
            name='ProductUserRequest',
        ),
    ]
