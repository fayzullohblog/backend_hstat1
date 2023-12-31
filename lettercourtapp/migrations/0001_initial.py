# Generated by Django 4.0 on 2023-12-21 06:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LetterCourt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('letter_name', models.CharField(max_length=50)),
                ('litter_number', models.CharField(max_length=15, unique=True)),
                ('company_name', models.CharField(max_length=150)),
                ('ptsh', models.CharField(max_length=15)),
                ('stir_number', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('report_name', models.CharField(max_length=100)),
                ('report_date', models.DateTimeField()),
                ('company_own', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accountapp.myuser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
