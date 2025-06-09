from django.views.generic import UpdateView
from django.urls import reverse_lazy
from accounts.models import CustomUser
from .forms import TeacherUpdateForm
from django.views.generic import DetailView


class TeacherProfileView(DetailView):
    model = CustomUser
    template_name = 'teachers/profile.html'
    context_object_name = 'teacher'

    def get_queryset(self):
        return CustomUser.objects.filter(role='teacher')
    

class TeacherUpdateView(UpdateView):
    model = CustomUser
    form_class = TeacherUpdateForm
    template_name = 'teachers/teacher_update.html'
    success_url = reverse_lazy('profile')  # یا مسیر دیگر مثل dashboard

    def get_queryset(self):
        return CustomUser.objects.filter(role='teacher')


