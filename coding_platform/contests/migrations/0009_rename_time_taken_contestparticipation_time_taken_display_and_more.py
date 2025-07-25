# Generated by Django 5.2.3 on 2025-07-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contests", "0008_contestparticipation_time_taken_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contestparticipation",
            old_name="time_taken",
            new_name="time_taken_display",
        ),
        migrations.AddField(
            model_name="contestparticipation",
            name="time_taken_seconds",
            field=models.IntegerField(default=0),
        ),
    ]
