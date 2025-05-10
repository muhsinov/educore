from django.contrib import admin
from .models import User, Student, Teacher, Address
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Address)






@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('phone', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('phone',)
    search_fields = ('phone', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'birth_date', 'address')}),
        (_('Permissions'), {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'joined_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'first_name', 'last_name', 'password1', 'password2', 'role', 'is_staff', 'is_active')}
        ),
    )

