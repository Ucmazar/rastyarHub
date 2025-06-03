# forms.py
from django import forms
from .models import CustomUser
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserUpdateForm, CustomUserCreateForm, LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



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
    form_class = CustomUserCreateForm
    template_name = 'accounts/user_create.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
    
    
class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
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
    form_class = CustomUserUpdateForm  # یا فرم ویرایش مخصوص پروفایل
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    
    
    
def login_view(request):
    form = LoginForm(request.POST or None)
    message = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user_list')  # یا صفحه مورد نظر شما
            else:
                message = "نام کاربری یا رمز عبور نادرست است."

    return render(request, 'accounts/login.html', {'form': form, 'message': message})