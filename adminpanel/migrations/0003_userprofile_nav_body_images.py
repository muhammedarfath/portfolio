# Generated by Django 5.1.2 on 2024-11-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_userprofile_nav_hover_images_userprofile_nav_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nav_body_images',
            field=models.ImageField(blank=True, null=True, upload_to='nav_body_images/'),
        ),
    ]
