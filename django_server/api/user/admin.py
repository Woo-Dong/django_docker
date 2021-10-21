from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'phone_number']
    search_fields = ['username', 'email', 'phone_number', 'last_name']

    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (  # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'nickname', 'nickname_used', 'phone_number', 'birth', 'lunar', 'profile_img', 'terms_agreed', 'withdrawn',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
