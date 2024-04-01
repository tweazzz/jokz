from django.contrib import admin
from .models import *
# Register your models here.

from django.contrib.auth.admin import UserAdmin

class UsersAdmin(UserAdmin):
    list_display = ('username', 'email','is_superuser')
    list_display_links = ('username',)
    search_fields = ('email', 'username', )
    readonly_fields = ('id', )
    ordering = ('id',)
    filter_horizontal = ()
    list_filter = ('is_active', 'is_superuser')
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2'),
        }),
    )


admin.site.register(User, UsersAdmin)
admin.site.register(Universities)
admin.site.register(Proffessions)
admin.site.register(Internships)
admin.site.register(News)