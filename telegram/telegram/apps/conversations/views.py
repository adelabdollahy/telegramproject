from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ConversationSerializer
from .models import Conversation


class ConversationsListCreateView(ListCreateAPIView):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()


class ConversationItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()
