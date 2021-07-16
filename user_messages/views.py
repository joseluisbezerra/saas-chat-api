from rest_framework import permissions, generics

from core.views import CompanySafeViewMixin
from . import serializers
from .models import UserMessage

from user_messages.filters import UserMessagesFilter
from django_filters.rest_framework import DjangoFilterBackend


class StalkerView(CompanySafeViewMixin, generics.ListAPIView):
    name = 'stalker'
    permission_classes = [
        permissions.IsAuthenticated & permissions.IsAdminUser]
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserMessagesFilter


class UserMessageList(generics.ListCreateAPIView):
    name = 'usermessage-list'
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserMessagesFilter

    def perform_create(self, serializer):
        user = self.request.user
        company_id = user.company_id
        serializer.save(company_id=company_id, from_user=user)

    def get_queryset(self):
        return UserMessage.objects.get_for_user(self.request.user)


class UserMessageDetail(generics.RetrieveAPIView):
    name = 'usermessage-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()

    def get_queryset(self):
        return UserMessage.objects.get_for_user(self.request.user)
