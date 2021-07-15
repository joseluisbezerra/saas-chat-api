from django_filters import rest_framework as filters
from django_filters import CharFilter

from user_messages.models import UserMessage


class UserMessagesFilter(filters.FilterSet):
    text = CharFilter(lookup_expr='icontains')

    class Meta:
        model = UserMessage
        fields = ['text', 'from_user', 'to_user', 'date']
