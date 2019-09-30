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
        user = self.client.post('http://127.0.0.1:8000/auth/users/', data={"first_name": "iyanu",
                                                                    "last_name": "ajao",
                                                                    "email": "iyanu@example.com",
                                                                    "password": "decagon1234"})

        response = self.client.post('http://127.0.0.1:8000/auth/token/login/', data={"password": "decagon1234",
                                                                              "email": "iyanu@example.com"})
        auth_token = response.data['auth_token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth_token)
        url = reverse('stocks:stock-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # @pytest.mark.django_db
    # def test_stock_buy(self):
    #     user = self.client.post('http://127.0.0.1:8000/auth/users/', data={"first_name": "iyanu",
    #                                                                 "last_name": "ajao",
    #                                                                 "email": "iyanu@example.com",
    #                                                                 "password": "decagon1234"})
    #
    #     response = self.client.post('http://127.0.0.1:8000/auth/token/login/', data={"password": "decagon1234",
    #                                                                           "email": "iyanu@example.com"})
    #     auth_token = response.data['auth_token']
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth_token)
    #
    #     url = reverse('stocks:stock-buy', kwargs={'symbol': 'ZOOM', 'shares': 1000})
    #     # account = AccountFactory()
    #     # stock = StockFactory(owner=account)
    #     # # # data = StockSerializer(data=stock)
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_stock_sell(self):
        user = self.client.post('http://127.0.0.1:8000/auth/users/', data={"first_name": "iyanu",
                                                                    "last_name": "ajao",
                                                                    "email": "iyanu@example.com",
                                                                    "password": "decagon1234"})

        response = self.client.post('http://127.0.0.1:8000/auth/token/login/', data={"password": "decagon1234",
                                                                              "email": "iyanu@example.com"})
        auth_token = response.data['auth_token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth_token)
        account = AccountFactory()
        stock = StockFactory(owner=account)
        url = reverse('stocks:stock-sell', kwargs={'pk': 1, 'shares': 100})

        # # data = StockSerializer(stock)
        # data = {"name": "string", "symbol": "string", "unit_price": 7, "shares": 10000, "total_price": 0}
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # @pytest.mark.django_db
    # def test_stock_search(self):
    #     user = self.client.post('http://127.0.0.1:8000/auth/users/', data={"first_name": "iyanu",
    #                                                                 "last_name": "ajao",
    #                                                                 "email": "iyanu@example.com",
    #                                                                 "password": "decagon1234"})
    #
    #     response = self.client.post('http://127.0.0.1:8000/auth/token/login/', data={"password": "decagon1234",
    #                                                                           "email": "iyanu@example.com"})
    #     auth_token = response.data['auth_token']
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth_token)
    #
    #     url = reverse('stocks:stock-search', kwargs={'symbol': 'ZOOM'})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
