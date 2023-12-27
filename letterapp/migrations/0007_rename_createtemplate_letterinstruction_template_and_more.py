# Generated by Django 4.0 on 2023-12-25 11:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0001_initial'),
        ('letterapp', '0006_alter_letterinstruction_created_date_add'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letterinstruction',
            old_name='createtemplate',
            new_name='template',
        ),
        migrations.AlterField(
            model_name='letterinstruction',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 11, 4, 43, 849606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='letterinstruction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.myuser'),
        ),
    ]