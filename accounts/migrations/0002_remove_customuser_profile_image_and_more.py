# Generated by Django 5.2.1 on 2025-06-02 17:12

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.profile_image_upload_path, verbose_name='تصویر پروفایل'),
        ),
    ]
