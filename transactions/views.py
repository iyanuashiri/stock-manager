import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.


class TransactionList(generics.ListAPIView):
    """Lists all transactions by a user or list transactions between a period of time

    :returns: list of transaction objects.
    :rtype: JSON
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date is not None:
            transactions = self.queryset.filter(user=self.request.user, created__range=(Transaction.parse_date(start_date), Transaction.parse_date(end_date)))
        else:
            transactions = self.queryset.filter(user=self.request.user)
        serializer = TransactionSerializer(transactions)
        return serializer
