from django_filters import rest_framework as filters
from django_filters import CharFilter

from accounts.models import User


class UserFilter(filters.FilterSet):
    username = CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username']
