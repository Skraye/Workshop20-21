from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

from .forms import AppUserCreationForm, AppUserChangeForm


class AppUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password", "username")}),
        ("Personal info", {"fields": ("first_name", "last_name", "role",)},),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "username"),
            },
        ),
    )
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = ["email", "first_name", "last_name", "role"]


admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Magasin)
admin.site.register(Role)
admin.site.register(Categorie)
admin.site.register(AlleeReserve)
admin.site.register(AlleeMagasin)
admin.site.register(Produit)
admin.site.register(Alerte)
admin.site.register(HistoryLogin)
admin.site.register(SupportApp)
