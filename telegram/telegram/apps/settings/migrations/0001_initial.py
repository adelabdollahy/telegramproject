# Generated by Django 4.1.6 on 2023-02-11 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_account_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text_size', models.IntegerField(default=16)),
                ('chat_list_view', models.IntegerField(choices=[(1, 'two lines'), (2, 'three lines')])),
                ('chat_list_swipe_gesture', models.IntegerField(choices=[(1, 'change folder'), (2, 'delete'), (3, 'mute'), (4, 'archive')])),
            ],
        ),
        migrations.CreateModel(
            name='NotificationSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_chats', models.BooleanField(default=True)),
                ('groups', models.BooleanField(default=True)),
                ('channels', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrivacySetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync_contact', models.BooleanField(default=False)),
                ('suggest_frequent_contacts', models.BooleanField(default=True)),
                ('link_preview', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.chatsetting')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.notificationsetting')),
                ('privacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.privacysetting')),
            ],
        ),
    ]
