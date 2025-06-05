# urls.py
from django.urls import path
from .views import (
    CustomUserCreateView,
    CustomUserListView,
    CustomUserUpdateView,
    CustomUserDeleteView,
    UserProfileView,
    UserProfileUpdateView,
    signup_view,
    login_view,
)

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('users/', CustomUserListView.as_view(), name='user_list'),
    path('users/create/', CustomUserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', CustomUserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', CustomUserDeleteView.as_view(), name='user_delete'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
    
    
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
