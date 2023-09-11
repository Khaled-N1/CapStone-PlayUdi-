# Generated by Django 4.2.5 on 2023-09-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0014_tournament_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='game',
            field=models.IntegerField(choices=[(4, '4'), (8, '8'), (16, '16'), (32, '32')], default=1),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='number_of_players',
            field=models.IntegerField(choices=[(4, '4'), (8, '8'), (16, '16'), (32, '32')], default=1),
        ),
    ]