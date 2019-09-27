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

