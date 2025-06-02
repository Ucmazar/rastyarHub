from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'gender', 'phone_number', 'is_staff', 'profile_picture_tag')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'gender', 'phone_number', 'profile_picture', 'created_by')}),
        
    )
    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="width: 40px; height:40px; border-radius: 50%;" />', obj.profile_picture.url)
        return "-"
    profile_picture_tag.short_description = 'تصویر پروفایل'

admin.site.register(CustomUser, CustomUserAdmin)
