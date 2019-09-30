from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from .utils import search_stock
from .models import Stock, Search
from .serializers import StockSerializer, StockSearchSerializer

# Create your views here.


class StockList(generics.ListAPIView):
    """Lists all stocks purchased by a user

    :returns: list of stock objects.
    :rtype: JSON
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        stocks = self.queryset.filter(owner=self.request.user)
        return stocks


class StockBuy(APIView):
    """Buy shares of a stock

    :param symbol: The symbol of the stock the user wants to buy
    :type symbol: str

    :param shares: The units of stock the user wants to buy
    :type shares: int

    :returns: the stock object bought
    :rtype: JSON
    """
    def post(self, request, symbol, shares):
        symbol, shares = symbol, shares
        price, company_name = search_stock(symbol)
        total_price = int(price) * int(shares)
        stock = Stock.objects.filter(owner=self.request.user, symbol=symbol)
        if stock.exists():
            stock = Stock.objects.get(owner=self.request.user, symbol=symbol)
            stock.add_more(shares, price)
        else:
            stock = Stock.objects.buy_stock(owner=self.request.user, name=company_name, symbol=symbol, unit_price=price, shares=shares, total_price=total_price)
        serializer = StockSerializer(stock, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StockSell(APIView):
    """Sell shares of a stock.

    :param pk: The primary key of the stock the user wants to sell
    :type pk: int

    :param shares: The units of stock the user wants to buy
    :type shares: int

    :returns: No content
    :rtype: None
    """
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def put(self, request, pk, shares):
        pk, shares = pk, shares
        stock = self.get_object(pk)
        price, name = search_stock(stock.symbol)
        stock.sell(shares, int(price))
        serializer = StockSerializer(stock, context={'request': request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class StockSearch(APIView):
    """Search for a stock

    :param symbol: The symbol of the stock the user wants to buy
    :type symbol: str

    :returns: object of search result
    :rtype: JSON
    """
    def get(self, request, symbol):
        price, company_name = search_stock(symbol)
        data = Search(price=price, company_name=company_name)
        serializer = StockSearchSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

