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


class StockBuy(generics.CreateAPIView):
    """Buy shares of a stock

    :param symbol: The symbol of the stock the user wants to buy
    :type symbol: str

    :param shares: The units of stock the user wants to buy
    :type shares: int

    :returns: the stock object bought
    :rtype: JSON
    """
    serializer_class = StockSerializer

    def post(self, request, *args, **kwargs):
        symbol, shares = kwargs['symbol'], kwargs['shares']
        price, company_name = search_stock(symbol)
        total_price = price * shares
        stock = Stock.objects.buy_stock(owner=self.request.user, name=company_name, symbol=symbol, unit_price=price, shares=shares, total_price=total_price)
        serializer = self.serializer_class(data=stock)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockSell(APIView):
    """Sell shares of a stock.

    :param pk: The primary key of the stock the user wants to sell
    :type pk: int

    :param shares: The units of stock the user wants to buy
    :type shares: int

    :returns: updated stock object sold and a string showing shares of stock left
    :rtype: JSON
    """
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def put(self, request, pk, shares):
        stock = self.get_object(pk)
        result = stock.sell(shares)
        serializer = StockSerializer(stock, data=request.data, context={'result': result})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockSearch(APIView):
    """Search for a stock

    :param symbol: The symbol of the stock the user wants to buy
    :type symbol: str

    :returns: object of search result
    :rtype: JSON
    """
    def get(self, request, symbol):
        price, company_name = search_stock(symbol)
        return Response({'price': price, 'company_name': company_name}, status=status.HTTP_200_OK)

