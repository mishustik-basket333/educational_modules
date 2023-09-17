from django.contrib import admin

from modules.models import Modules


# Register your models here.
@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("title",)
    search_fields = ("title",)
