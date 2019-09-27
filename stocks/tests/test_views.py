from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

import pytest

from accounts.factories import AccountFactory
from ..factories import StockFactory
from ..serializers import StockSerializer


class TestStockList(APITestCase):

    @pytest.mark.django_db
    def test_stock_list(self):
        url = reverse('stock-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_stock_buy(self):
        url = reverse('stock-buy', kwargs={'symbol': StockFactory.symbol, 'shares': StockFactory.shares})
        account = AccountFactory()
        stock = StockFactory(owner=account)
        data = StockSerializer(stock)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

