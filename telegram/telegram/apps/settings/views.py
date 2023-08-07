from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SettingSerializer
from .models import Setting


class SettingsListCreateView(ListCreateAPIView):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()


class SettingItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()


