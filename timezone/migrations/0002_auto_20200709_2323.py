# Generated by Django 3.0.7 on 2020-07-09 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timezone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datetime',
            name='InputDT',
        ),
        migrations.AddField(
            model_name='datetime',
            name='userDT',
            field=models.CharField(default='00:00:00', max_length=100),
        ),
        migrations.AddField(
            model_name='datetime',
            name='userTZ',
            field=models.CharField(default='UTC', max_length=100),
        ),
    ]
