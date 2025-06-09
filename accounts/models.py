from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def profile_image_upload_path(instance, filename):
    today = datetime.today()
    return f'profile_image/{today.year}/{today.month}/{today.day}/{filename}'

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    profile_picture = models.ImageField(
        _('تصویر پروفایل'),
        upload_to=profile_image_upload_path,
        blank=True,
        null=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_users'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.role}"


class BaseProfile(models.Model):
    father_name = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=150, blank=True, null=True)
    father_job = models.CharField(max_length=100, blank=True, null=True)
    permanent_address = models.CharField(max_length=200, blank=True, null=True)
    current_address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True  # مدل پایه است، جدول جداگانه در دیتابیس نمی‌سازد

    def __str__(self):
        return f"{self.father_name or '---'}"
