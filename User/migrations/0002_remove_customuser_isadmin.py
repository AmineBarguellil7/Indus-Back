# Generated by Django 4.2.3 on 2023-08-09 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='isAdmin',
        ),
    ]