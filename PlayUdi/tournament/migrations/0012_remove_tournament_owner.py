# Generated by Django 4.2.5 on 2023-09-09 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0011_tournament_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='owner',
        ),
    ]
