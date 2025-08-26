from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "phone", "is_active"]
    search_fields = ["id", "username", "email", "phone"]
    list_filter = ["is_active"]
