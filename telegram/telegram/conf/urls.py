"""telegram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.accounts.urls import urlpatterns as accounts_urlpatterns
from apps.settings.urls import urlpatterns as settings_urlpatterns
from apps.contacts.urls import urlpatterns as contacts_urlpatterns
from apps.conversations.urls import urlpatterns as conversations_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += accounts_urlpatterns
urlpatterns += settings_urlpatterns
urlpatterns += contacts_urlpatterns
urlpatterns += conversations_urlpatterns


