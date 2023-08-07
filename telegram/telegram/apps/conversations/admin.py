from django.contrib import admin
from apps.conversations.models import Conversation


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['type']


