from django.contrib import admin
from .models import User, Dream, CommonTag, UserTag
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(Dream)
admin.site.register(CommonTag)
admin.site.register(UserTag)