# Generated by Django 4.2.5 on 2023-09-09 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0006_merge_20230909_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='players_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tournament.profile'),
            preserve_default=False,
        ),
    ]
