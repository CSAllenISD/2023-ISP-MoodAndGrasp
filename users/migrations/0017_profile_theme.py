# Generated by Django 4.1 on 2023-04-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_remove_profile_grasp_remove_profile_mood_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="theme",
            field=models.CharField(
                choices=[
                    ("a", "Beach"),
                    ("b", "Winter"),
                    ("c", "Castle"),
                    ("d", "Ocean"),
                    ("e", "Space"),
                    ("f", "Haunted"),
                    ("g", "Mystic"),
                    ("h", "Default Gradient"),
                ],
                default="h",
                max_length=1,
            ),
        ),
    ]
