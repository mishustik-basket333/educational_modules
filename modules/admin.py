from django.contrib import admin

from modules.models import Modules


# Register your models here.
@admin.register(Modules)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "description")
    list_filter = ("title",)
    search_fields = ("title", "owner",)
