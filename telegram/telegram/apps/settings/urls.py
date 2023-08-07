from django.urls import path
from .views import SettingsListCreateView, SettingItemView

urlpatterns = [
    path('api/settings/', SettingsListCreateView.as_view(), name='SettingsListCreateView'),
    path('api/settings/<int:pk>', SettingItemView.as_view(), name='SettingItemView')
]
