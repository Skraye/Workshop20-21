from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models.models import AppUser


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AppUser
        fields = ("email", "first_name", "last_name", "role")


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = UserChangeForm.Meta.fields
