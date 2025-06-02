# forms.py
from django import forms
from .models import CustomUser
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role', 'gender', 'phone_number', 'profile_picture']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/user_create.html'
    success_url = reverse_lazy('user_list')

class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
    
    
class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserCreationForm  # اگر می‌خواهی فرم متفاوت باشه، می‌تونی فرم جدا بسازی
    template_name = 'accounts/user_update.html'
    success_url = reverse_lazy('user_list')
    
class CustomUserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'accounts/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
    
class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'

    def get_object(self):
        # فقط پروفایل خود کاربر
        return self.request.user
    
class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserCreationForm  # یا فرم ویرایش مخصوص پروفایل
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    
    
    