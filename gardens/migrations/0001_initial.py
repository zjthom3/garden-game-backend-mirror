# Generated by Django 3.1.4 on 2021-01-07 23:58

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
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField(default=2)),
                ('columns', models.IntegerField(default=4)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flower_name', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
                ('level', models.IntegerField()),
                ('time_to_mature', models.IntegerField()),
                ('exp_value', models.IntegerField()),
                ('currency', models.IntegerField()),
                ('desc', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Plants_in_garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvested', models.BooleanField()),
                ('watered', models.BooleanField()),
                ('remaining_time', models.IntegerField()),
                ('row_num', models.IntegerField()),
                ('column_num', models.IntegerField()),
                ('garden_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gardens.garden')),
                ('plant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gardens.plant')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_level', models.IntegerField(default=0)),
                ('xp', models.IntegerField(default=0)),
                ('currency', models.IntegerField(default=0)),
                ('city', models.CharField(blank=True, max_length=150)),
                ('state', models.CharField(blank=True, max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
