# forms.py
from django import forms
from .models import CustomUser
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserUpdateForm, CustomUserCreateForm, LoginForm, CustomUserSignupForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .mixins import RoleRequiredMixin



class CustomUserCreationForm(LoginRequiredMixin, forms.ModelForm):
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


class UserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'accounts/user_create.html'
    success_url = reverse_lazy('user_list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UserListView(RoleRequiredMixin, LoginRequiredMixin, ListView):
    required_role = None
    model = CustomUser
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
    required_roles = ['manager', 'teacher']
    def get_queryset(self):
        return CustomUser.objects.filter(created_by=self.request.user)

class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'accounts/user_update.html'
    success_url = reverse_lazy('user_list')
    def get_queryset(self):
        return CustomUser.objects.filter(created_by=self.request.user)

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'accounts/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
    def get_queryset(self):
        return CustomUser.objects.filter(created_by=self.request.user)
    
class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'

    def get_object(self):
        # فقط پروفایل خود کاربر
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm  # یا فرم ویرایش مخصوص پروفایل
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        # فقط پروفایل خود کاربر
        return self.request.user
    
    
class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'accounts/user_profile.html'  # مسیر قالب را خودت تنظیم کن
    context_object_name = 'profile'
    
    def get_queryset(self):
        return CustomUser.objects.filter(created_by=self.request.user)
    
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"{user.get_full_name()} عزیز خوش آمدید!")
                return redirect('user_list')  # یا مسیر مورد نظر شما
            else:
                messages.error(request, "نام کاربری یا رمز عبور نادرست است.")

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    message = None
    if request.method == 'POST':
        form = CustomUserSignupForm(request.POST, request.FILES)

        if request.method == 'POST':
            form = CustomUserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            message = "لطفاً خطاهای زیر را بررسی کنید."
    else:
        form = CustomUserSignupForm()

    return render(request, 'accounts/signup.html', {'form': form})



def custom_page_not_found_view(request, exception):
    return render(request, "404.html", status=404)





def role_based_user_profile_view(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)

    if user.role == 'teacher':
        return redirect('teacher_profile', pk=user.pk)
    elif user.role == 'manager':
        return redirect('manager_profile', pk=user.pk)
    elif user.role == 'student':
        return redirect('student_profile', pk=user.pk)
    elif user.role == 'parent':
        return redirect('parent_profile', pk=user.pk)
    else:
        return redirect('home')  # یا صفحه‌ی پیش‌فرض
    
    
    
def role_based_user_update_view(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)

    if user.role == 'teacher':
        return redirect('teacher_update', pk=pk)
    elif user.role == 'student':
        return redirect('student_update', pk=pk)
    elif user.role == 'parent':
        return redirect('parent_update', pk=pk)
    elif user.role == 'manager':
        return redirect('manager_update', pk=pk)
    else:
        # fallback
        return redirect('profile')  # یا پیام خطا نمایش بده