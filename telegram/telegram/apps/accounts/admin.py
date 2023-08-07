from django.contrib import admin

from apps.accounts.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number', 'reference_id', 'profile_image', 'profile_image']

