import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.


class TransactionList(APIView):
    """Lists all transactions by a user or list transactions between a period of time

    :returns: list of transaction objects.
    :rtype: JSON
    """
    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        if start_date and end_date is not None:
            actions = Transaction.objects.filter(user=self.request.user, created__range=(Transaction.parse_date(start_date), Transaction.parse_date(end_date)))
        else:
            actions = Transaction.objects.filter(user=self.request.user)
        serializer = TransactionSerializer(actions)
        return Response(serializer.data, status=status.HTTP_200_OK)
