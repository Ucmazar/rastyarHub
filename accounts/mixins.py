from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class RoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    required_role = None  # مثلاً 'manager'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == self.required_role
