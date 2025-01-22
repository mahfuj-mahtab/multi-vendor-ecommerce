from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the admin panel
    list_display = ('email', 'is_staff', 'is_active')
    ordering = ('email',)
    search_fields = ('email',)

    # Define fieldsets for viewing and editing users
    fieldsets = (
        (None, {'fields': ('email', 'password','username')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Custom Info', {'fields': ('phone', 'avatar','date_of_birth','email_verified','phone_verified')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define fieldsets for creating users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
