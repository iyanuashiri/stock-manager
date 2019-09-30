from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
import pytest

from accounts.factories import AccountFactory
from stocks.factories import StockFactory


class TestTransactionList(APITestCase):

    @pytest.mark.django_db
    def test_can_get_transaction_list(self):
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

        url = reverse('transactions:transaction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


