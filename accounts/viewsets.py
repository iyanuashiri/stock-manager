from rest_framework import viewsets, permissions

from .serializers import AccountSerializer
from .models import Account


class AccountViewset(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint provides list, detail actions for Account
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.queryset.exclude(email=self.request.user)
