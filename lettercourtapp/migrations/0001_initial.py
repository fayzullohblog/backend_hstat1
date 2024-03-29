# Generated by Django 4.2 on 2024-03-08 06:03

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
            name="LetterCourt",
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
                ("litter_number", models.CharField(max_length=15, unique=True)),
                ("company_name", models.CharField(max_length=150)),
                ("ptsh", models.CharField(max_length=15)),
                (
                    "stir_number",
                    models.PositiveBigIntegerField(blank=True, default=0, null=True),
                ),
                ("report_name", models.CharField(max_length=100)),
                ("report_date", models.DateTimeField()),
                ("company_own", models.CharField(max_length=50)),
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
