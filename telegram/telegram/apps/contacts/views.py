from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ContactSerializer
from .models import Contact


class ContactsListCreateView(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


