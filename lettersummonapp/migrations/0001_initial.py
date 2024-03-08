# Generated by Django 4.2 on 2024-03-08 06:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LetterSummons",
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
                ("create_date", models.DateTimeField(auto_now=True)),
                ("update_date", models.DateTimeField(auto_now_add=True)),
                ("letter_name", models.CharField(max_length=50)),
                ("company_name", models.CharField(max_length=150)),
                ("report_name", models.CharField(max_length=100)),
                ("adress", models.CharField(max_length=100)),
                ("street", models.CharField(max_length=100)),
                ("litter_number", models.CharField(max_length=15, unique=True)),
                ("inn_number", models.CharField(max_length=15)),
                ("stir_number", models.PositiveBigIntegerField(default=0)),
                ("phone_number", models.CharField(max_length=13)),
                ("report_date", models.DateTimeField()),
                (
                    "created_date_add",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024, 3, 13, 6, 3, 14, 498534, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "state",
                    models.BooleanField(
                        choices=[(True, "Topshirdi"), (False, "Topshirmadi")],
                        default=False,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
