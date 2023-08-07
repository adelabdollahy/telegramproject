from django.urls import path
from .views import AccountsListCreateView, AccountItemView

urlpatterns = [
    path('api/accounts/', AccountsListCreateView.as_view(), name="AccountsListCreateView"),
    path('api/accounts/<int:pk>/', AccountItemView.as_view(), name="AccountItemView")
]
