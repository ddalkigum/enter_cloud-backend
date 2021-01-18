# Generated by Django 3.1.5 on 2021-01-18 10:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spaces', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=18)),
                ('day', models.DateField(default=datetime.datetime(2021, 1, 18, 10, 33, 22, 204236, tzinfo=utc))),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('detail_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spaces.detailspace')),
            ],
            options={
                'db_table': 'packages',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('day', models.DateField(default=datetime.datetime(2021, 1, 18, 10, 33, 22, 204777, tzinfo=utc))),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('detail_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spaces.detailspace')),
            ],
            options={
                'db_table': 'times',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('people', models.IntegerField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.package')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'reservations',
            },
        ),
    ]