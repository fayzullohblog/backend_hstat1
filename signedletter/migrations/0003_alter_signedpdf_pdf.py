# Generated by Django 4.0 on 2024-02-08 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signedletter', '0002_unsignedpdfurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signedpdf',
            name='pdf',
            field=models.FileField(upload_to=''),
        ),
    ]
