from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import AuthUser


class AuthUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'last_login', 'is_admin', 'is_staff')
    readonly_fields = ('id', 'date_joined', 'last_login')
    search_fields = ('email', 'username',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Info'), {'fields': ('bio', 'profile_image')}),
    )


admin.site.register(AuthUser, AuthUserAdmin)
