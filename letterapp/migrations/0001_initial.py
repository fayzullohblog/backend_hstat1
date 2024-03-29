# Generated by Django 4.2 on 2024-03-08 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mainletter", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PdfFileTemplate",
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
                (
                    "pdf_file",
                    models.FileField(upload_to="pdfletterinstruction/unsigned/"),
                ),
                ("soato", models.CharField(max_length=50)),
                ("inn_number", models.CharField(max_length=15)),
                (
                    "state",
                    models.BooleanField(
                        choices=[(True, "Topshirdi"), (False, "Topshirmadi")],
                        default=False,
                    ),
                ),
                ("signed_state", models.BooleanField(default=False)),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pdffiletemplate_template",
                        to="mainletter.template",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pdffiletemplate_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
