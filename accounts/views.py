from rest_framework import generics, permissions

from django.contrib.auth import get_user_model
from core.views import CompanySafeViewMixin

from . import serializers
from .permissions import IsAdmin, IsOwner, ReadOnly

from accounts.filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class AccountCreate(generics.CreateAPIView):
    name = 'account-create'
    serializer_class = serializers.AccountSerializer


class UserList(CompanySafeViewMixin, generics.ListCreateAPIView):
    name = 'user-list'
    permission_classes = [
        permissions.IsAuthenticated & permissions.IsAdminUser]
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter


class UserDetail(CompanySafeViewMixin, generics.RetrieveUpdateDestroyAPIView):
    name = 'user-detail'
    permission_classes = [permissions.IsAuthenticated &
                          ((IsOwner | ReadOnly) | IsAdmin)]
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class CompanyDetail(generics.RetrieveUpdateAPIView):
    name = 'company-detail'
    permission_classes = [permissions.IsAuthenticated &
                          (permissions.IsAdminUser | ReadOnly)]
    serializer_class = serializers.CompanySerializer

    def get_object(self):
        # Ensure that users can only see the company that they belong to
        return self.request.user.company
