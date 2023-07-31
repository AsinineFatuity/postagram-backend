# Generated by Django 4.0 on 2023-03-08 18:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core_user", "0002_user_avatar_user_bio"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "public_id",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
                ("body", models.TextField()),
                ("edited", models.BooleanField(default=False)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core_user.user"
                    ),
                ),
            ],
            options={
                "db_table": "'core.post'",
            },
        ),
    ]
