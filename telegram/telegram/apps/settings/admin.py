from django.contrib import admin

from apps.settings.models import Setting, PrivacySetting, NotificationSetting, ChatSetting


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'privacy', 'notification', 'chat']


@admin.register(PrivacySetting)
class PrivacySettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'sync_contact', 'suggest_frequent_contacts', 'link_preview']


@admin.register(NotificationSetting)
class NotificationSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'private_chats', 'groups', 'channels']


@admin.register(ChatSetting)
class ChatSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_text_size', 'chat_list_view', 'chat_list_swipe_gesture']


