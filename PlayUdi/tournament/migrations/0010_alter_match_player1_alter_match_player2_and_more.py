# Generated by Django 4.2.5 on 2023-09-09 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0009_tournament_number_of_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player1', to='tournament.profile'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player2', to='tournament.profile'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tournament.profile'),
        ),
    ]
