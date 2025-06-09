from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from managers.models import ManagerProfile
from accounts.forms import CustomUserUpdateForm
from managers.forms import ManagerProfileUpdateForm
from django.core.exceptions import PermissionDenied


class ManagerProfileView(LoginRequiredMixin, View):
    template_name = 'managers/profile.html'

    def get(self, request, pk):
        # نمایش پروفایل یک مدیر بر اساس pk
        manager = get_object_or_404(CustomUser, pk=pk, role='manager')
        return render(request, self.template_name, {'manager': manager})



class ManagerUpdateView(LoginRequiredMixin, View):
    template_name = 'managers/manager_update.html'

    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk, role='manager')

        # if request.user != user:
        #     raise PermissionDenied()

        profile = getattr(user, 'manager_profile', None)
        if not profile:
            profile = ManagerProfile.objects.create(user=user)

        user_form = CustomUserUpdateForm(instance=user)
        profile_form = ManagerProfileUpdateForm(instance=profile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
        })

    def post(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk, role='manager')

        # if request.user != user:
        #     raise PermissionDenied()

        profile = getattr(user, 'manager_profile', None)
        if not profile:
            profile = ManagerProfile.objects.create(user=user)

        user_form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        profile_form = ManagerProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('manager_profile', pk=pk)

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
        })


class ManagerProfileEditView(LoginRequiredMixin, View):
    template_name = 'managers/manager_update.html'

    def get(self, request):
        user = request.user
        # فرض می‌کنیم related_name='manager_profile' در مدل ManagerProfile تعریف شده
        profile = getattr(user, 'manager_profile', None)
        if profile is None:
            profile = ManagerProfile.objects.create(user=user)

        user_form = CustomUserUpdateForm(instance=user)
        profile_form = ManagerProfileUpdateForm(instance=profile)

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        user = request.user
        profile = getattr(user, 'manager_profile', None)
        if profile is None:
            profile = ManagerProfile.objects.create(user=user)

        user_form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        profile_form = ManagerProfileUpdateForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('manager_profile', pk=user.pk)

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })
