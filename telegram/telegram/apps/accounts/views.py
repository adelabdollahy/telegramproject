from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AccountSerializer
from .models import Account


class AccountsListCreateView(ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


