from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main_app.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
