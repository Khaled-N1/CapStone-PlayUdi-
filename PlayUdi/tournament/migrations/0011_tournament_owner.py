# Generated by Django 4.2.5 on 2023-09-09 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0010_alter_match_player1_alter_match_player2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tournament.profile'),
            preserve_default=False,
        ),
    ]
