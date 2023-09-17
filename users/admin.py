from django.contrib import admin

from users.models import User, Moderator, Teacher

# Register your models here.
admin.site.register(User)

admin.site.register(Moderator)

admin.site.register(Teacher)
