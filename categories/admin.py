from django.contrib import admin

from categories.models import Category

admin.site.register(Category)

# @admin.register(Modules)
# class ModulesAdmin(admin.ModelAdmin):
#     list_display = ("title", "description")
#     list_filter = ("title",)
#     search_fields = ("title",)

