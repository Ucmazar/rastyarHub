from django import forms
from accounts.models import CustomUser

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'profile_picture' ]
