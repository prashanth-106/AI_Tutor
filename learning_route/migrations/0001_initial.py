# Generated by Django 5.0.1 on 2024-09-09 01:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("learning_resource", "0001_initial"),
        ("skill", "0004_alter_skill_id_alter_skilllevel_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="LearningRouteResource",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("completed", models.BooleanField(default=False)),
                (
                    "time_spent",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "learning_resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learning_resource.learningresource",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LearningRoute",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "duration",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                ("actual_resource_index", models.IntegerField(default=0)),
                ("completed", models.BooleanField(default=False)),
                (
                    "time_spent",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "skill_level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="skill.skilllevel",
                    ),
                ),
                (
                    "learning_route_resources",
                    models.ManyToManyField(
                        blank=True,
                        related_name="learning_routes",
                        to="learning_route.learningrouteresource",
                    ),
                ),
            ],
        ),
    ]
