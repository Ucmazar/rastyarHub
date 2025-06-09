# urls.py
from django.urls import path
from .views import (
    UserCreateView,
    UserListView,
    UserUpdateView,
    UserDeleteView,
    ProfileView,
    ProfileUpdateView,
    UserProfileView,
    signup_view,
    login_view,
    logout_view,
    role_based_user_update_view,
    role_based_user_profile_view,
)

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    
    # path('user/<int:pk>/profile/', UserProfileView.as_view(), name='user_profile'),
    # path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    
    path('profile/<int:pk>', role_based_user_profile_view, name='redirect_to_profile'),
    path('user/<int:pk>/update/', role_based_user_update_view, name='redirect_to_profile_update'),
    
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
