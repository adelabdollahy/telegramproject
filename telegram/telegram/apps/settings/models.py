from django.db import models


class Setting(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    privacy = models.ForeignKey('settings.PrivacySetting', on_delete=models.CASCADE)
    notification = models.ForeignKey('settings.NotificationSetting', on_delete=models.CASCADE)
    chat = models.ForeignKey("settings.ChatSetting", on_delete=models.CASCADE)


class PrivacySetting(models.Model):
    sync_contact = models.BooleanField(default=False)
    suggest_frequent_contacts = models.BooleanField(default=True)
    link_preview = models.BooleanField(default=False)


class NotificationSetting(models.Model):
    private_chats = models.BooleanField(default=True)
    groups = models.BooleanField(default=True)
    channels = models.BooleanField(default=True)


class ChatSetting(models.Model):
    CHAT_LIST_VIEW_TYPES = (
        (1, 'two lines'),
        (2, 'three lines')
    )
    CHAT_LIST_SWIPE_GESTURE_TYPES = (
        (1, 'change folder'),
        (2, 'delete'),
        (3, 'mute'),
        (4, 'archive'),
    )
    message_text_size = models.IntegerField(default=16)
    chat_list_view = models.IntegerField(choices=CHAT_LIST_VIEW_TYPES)
    chat_list_swipe_gesture = models.IntegerField(choices=CHAT_LIST_SWIPE_GESTURE_TYPES)
