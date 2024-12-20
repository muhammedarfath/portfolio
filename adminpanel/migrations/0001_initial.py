# Generated by Django 5.1.2 on 2024-11-08 16:17

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
            name='BottomProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('hover_img', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
            ],
        ),
        migrations.CreateModel(
            name='HomepageProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('keyword', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('hover_img', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkpageProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('keyword', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('hover_img', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('contact_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('name', models.CharField(max_length=100)),
                ('subdescription', models.CharField(blank=True, max_length=255, null=True)),
                ('maindescription', models.TextField(blank=True, null=True)),
                ('references', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BottomProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='bottom_projects/file/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='adminpanel.bottomproject')),
            ],
        ),
        migrations.CreateModel(
            name='HomeProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=500, upload_to='homepage_projects/videos/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='adminpanel.homepageproject')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=500, upload_to='homepage_projects/videos/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='adminpanel.workpageproject')),
            ],
        ),
    ]
