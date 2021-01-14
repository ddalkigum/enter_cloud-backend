# Generated by Django 3.1.5 on 2021-01-14 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('spaces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=300)),
                ('rating', models.IntegerField()),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spaces.space')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=300)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.host')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.review')),
            ],
            options={
                'db_table': 'review_comments',
            },
        ),
    ]
