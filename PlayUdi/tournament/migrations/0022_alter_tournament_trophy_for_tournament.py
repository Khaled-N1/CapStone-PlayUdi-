# Generated by Django 4.2.5 on 2023-09-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0021_profile_bio_alter_profile_user_rank_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='trophy_for_tournament',
            field=models.IntegerField(choices=[(100, 'Bronze'), (200, 'Sliver'), (300, 'Gold')], default=100),
        ),
    ]