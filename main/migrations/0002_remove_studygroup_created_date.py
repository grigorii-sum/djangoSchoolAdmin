# Generated by Django 3.1.7 on 2021-02-24 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studygroup',
            name='created_date',
        ),
    ]
