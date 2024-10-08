# Generated by Django 5.0.7 on 2024-08-13 05:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0002_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="followers",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="followings",
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name="Follower",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fans",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "idol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="idols",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("idol", "fan")},
            },
        ),
    ]
