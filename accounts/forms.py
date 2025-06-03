from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # فیلدهایی که اجازه ویرایش دارند (موارد حساس حذف شده‌اند)
        fields = [
            'username', 'email', 'phone_number',
            'first_name', 'last_name', 'role', 'gender', 'profile_picture'
        ]
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'role': 'نقش',
            'gender': 'جنسیت',
            'profile_picture': 'عکس پروفایل',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'form-control-file'
            elif isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'



class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # فیلدهایی که اجازه ویرایش دارند (موارد حساس حذف شده‌اند)
        fields = [
            'username', 'email', 'phone_number', 'profile_picture',
            'first_name', 'last_name', 'role', 'gender'
        ]
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'profile_picture': 'عکس پروفایل',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'role': 'نقش',
            'gender': 'جنسیت',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'form-control-file'
            elif isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'



class LoginForm(forms.Form):
    username = forms.CharField(
        label="نام کاربری",  # ← فارسی
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام کاربری را وارد کنید'
        })
    )
    password = forms.CharField(
        label="رمز عبور",  # ← فارسی
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور را وارد کنید'
        })
    )




class CustomUserSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'profile_picture', 'role', 'gender', 'password1', 'password2']
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'profile_picture': 'تصویر پروفایل',
            'role': 'نقش',
            'gender': 'جنسیت',
            'password1': 'رمز عبور',
            'password2': 'تکرار رمز عبور',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'form-control-file'
            elif isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'