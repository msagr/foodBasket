from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile

# class UserAdmin(BaseUserAdmin):
# 	list_display = ('email', 'username', 'first_name', 'last_name', 'role', 'is_admin')
# 	search_fields = ('email', 'username', 'first_name', 'last_name')
# 	readonly_fields = ('date_joined', 'last_login', 'created_date', 'modified_date')

# 	ordering = ('email',)
# 	filter_horizontal = ()
# 	list_filter = ('role', 'is_admin', 'is_active')
# 	fieldsets = (
# 		(None, {'fields': ('email', 'password')}),
# 		('Personal info', {'fields': ('first_name', 'last_name', 'username', 'phone_number', 'role')}),
# 		('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_superadmin')}),
# 		('Dates', {'fields': ('date_joined', 'last_login', 'created_date', 'modified_date')}),
# 	)

# 	add_fieldsets = (
# 		(None, {
# 			'classes': ('wide',),
# 			'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'role'),
# 		}),
# 	)

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)