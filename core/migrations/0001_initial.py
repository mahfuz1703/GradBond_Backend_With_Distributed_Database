# Generated by Django 5.1 on 2024-12-02 08:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('graduation_year', models.IntegerField()),
                ('company', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('linkedin', models.URLField()),
                ('image', models.ImageField(blank=True, default='alumni/default.png', null=True, upload_to='alumni/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(blank=True, default='student/default.png', null=True, upload_to='student/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]