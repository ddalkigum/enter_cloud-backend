# Generated by Django 3.1.5 on 2021-01-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20210118_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]