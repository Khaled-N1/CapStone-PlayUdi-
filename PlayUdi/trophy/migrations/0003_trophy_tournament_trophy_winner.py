# Generated by Django 4.2.5 on 2023-09-10 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0015_tournament_game_alter_tournament_number_of_players'),
        ('trophy', '0002_trophy_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='trophy',
            name='tournament',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament'),
        ),
        migrations.AddField(
            model_name='trophy',
            name='winner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tournament.profile'),
        ),
    ]
