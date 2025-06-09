# forms.py
from django import forms
from accounts.models import CustomUser
from managers.models import ManagerProfile  # یا هر پروفایلی که BaseProfile را ارث برده

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'phone_number', 'profile_picture',
            'first_name', 'last_name', 'gender'
        ]
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'profile_picture': 'عکس پروفایل',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'gender': 'جنسیت',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ManagerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ManagerProfile
        fields = [
            'father_name', 'education', 'father_job',
            'permanent_address', 'current_address'
        ]
        labels = {
            'father_name': 'نام پدر',
            'education': 'تحصیلات',
            'father_job': 'شغل پدر',
            'permanent_address': 'آدرس اصلی',
            'current_address': 'آدرس فعلی',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
