from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone', 'email', 'is_active', 'is_staff', 'avatar_img')
    search_fields = ('username', 'phone', 'email', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'phone', 'avatar'),
        }),
    )

    def avatar_img(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.avatar.url) if obj.avatar else None
    avatar_img.short_description = 'Изображение'
