from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Course, Grade


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'user_type', 'address', 'state', 'zipcode', 'email', 'cell_phone', 'date' ]
    list_filter = ['username', 'user_type', 'address', 'state', 'zipcode', 'email', 'cell_phone']
    fieldsets = (
         ('Account Information', {
            'fields': ('username', 'password', 'is_staff', 'is_superuser')
        }),
         ('Type of user', {
            'fields': ('user_type', 'cell_phone')
        }),
         ('Contact Information', {
            'fields': ('address', 'state', 'zipcode', 'email')
        })
   )
add_fieldsets = (
         ('Account Information', {
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser')
        }),
         ('Position', {
            'fields': ('user_type', 'cell_phone')
        }),
         ('Contact Information', {
            'fields': ('address', 'state', 'zipcode', 'email' )
        })
   )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course)
admin.site.register(Grade)
