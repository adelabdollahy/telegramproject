from django.urls import path
from .views import ContactsListCreateView, ContactItemView

urlpatterns = [
    path("api/contacts/", ContactsListCreateView.as_view(), name='ContactsListCreateView'),
    path("api/contacts/<int:pk>/", ContactItemView.as_view(), name='ContactsListCreateView')
]
