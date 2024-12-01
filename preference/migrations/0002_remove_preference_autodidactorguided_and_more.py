# Generated by Django 5.0.1 on 2024-09-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("preference", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="preference",
            name="autodidactOrGuided",
        ),
        migrations.AddField(
            model_name="preference",
            name="learningType",
            field=models.CharField(
                choices=[
                    ("autodidact", "Autodidact"),
                    ("guided", "Guided"),
                    ("challenges", "Challenges"),
                ],
                default=None,
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="preference",
            name="contentType",
            field=models.CharField(
                choices=[
                    ("guides", "Guides"),
                    ("documentation", "Documentation"),
                    ("introduction", "Introduction"),
                    ("summary", "Summary"),
                    ("article", "Article"),
                    ("quiz", "Quiz"),
                    ("podcast", "Podcast"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="preference",
            name="mediaType",
            field=models.CharField(
                choices=[("video", "Video"), ("audio", "Audio"), ("text", "Text")],
                max_length=100,
            ),
        ),
    ]