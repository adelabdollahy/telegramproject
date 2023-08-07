from django.urls import path
from .views import ConversationsListCreateView, ConversationItemView

urlpatterns = [
    path("api/conversations/", ConversationsListCreateView.as_view(), name="ConversationsListCreateView"),
    path("api/conversations/<int:pk>/", ConversationItemView.as_view(), name='ConversationItemView')

]
