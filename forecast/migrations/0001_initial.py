# Generated by Django 2.0 on 2018-01-03 09:04

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
            name='userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='wheather',
            fields=[
                ('created_datetime', models.DateTimeField(verbose_name='created date of record')),
                ('weather_date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('min_temp', models.IntegerField(default=0)),
                ('max_temp', models.IntegerField(default=0)),
                ('wind', models.IntegerField(default=0)),
                ('rain', models.CharField(max_length=10)),
            ],
        ),
    ]
