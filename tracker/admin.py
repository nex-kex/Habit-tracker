from django.contrib import admin

from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "action", "is_enjoyable", "is_public"]
    search_fields = ["id", "user", "action"]
    list_filter = ["is_enjoyable", "is_public"]