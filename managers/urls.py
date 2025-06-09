from django.urls import path
from .views import ManagerUpdateView, ManagerProfileView

urlpatterns = [
    path('<int:pk>/view', ManagerProfileView.as_view(), name='manager_profile'),
    path('<int:pk>/update/', ManagerUpdateView.as_view(), name='manager_update'),
]

