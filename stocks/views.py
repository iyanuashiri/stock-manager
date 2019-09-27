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


class StockBuy(APIView):
    """

    """
    def post(self, request, symbol, shares, format=None):
        price, company_name = search_stock(symbol)
        total_price = price * shares
        stock = Stock.objects.buy_stock(owner=self.request.user, name=company_name, symbol=symbol, unit_price=price, shares=shares, total_price=total_price)
        serializer = StockSerializer(data=stock)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockSell(APIView):
    """

    """
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def put(self, request, pk, shares, format=None):
        stock = self.get_object(pk)
        result = stock.sell(shares)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockSearch(APIView):
    """

    """
    def get(self, request, symbol, format=None):
        price, company_name = search_stock(symbol)
        return Response({'price': price, 'company_name': company_name}, status=status.HTTP_200_OK)

