from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from .utils import search_stock
from .models import Stock
from .serializers import StockSerializer

# Create your views here.


class StockList(generics.ListAPIView):
    """

    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        stocks = self.queryset.filter(owner=self.request.user)
        return stocks






