from django.urls import path
from .views import TeacherUpdateView, TeacherProfileView

urlpatterns = [
    path('<int:pk>/view', TeacherProfileView.as_view(), name='teacher_profile'),
    path('<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
]

