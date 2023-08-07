from django.contrib import admin

from apps.contacts.models import Contact


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'related_account', 'owner']


