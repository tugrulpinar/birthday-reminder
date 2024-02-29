from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from pages.models import BirthDayRecord


class BirthDayRecordInline(admin.TabularInline):
        model = BirthDayRecord


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    inlines = [BirthDayRecordInline]

admin.site.register(CustomUser, CustomUserAdmin)