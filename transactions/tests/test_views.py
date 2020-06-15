from django.urls import reverse

import pytest


@pytest.mark.django_db
def test_transaction_list(authenticated):
    client = authenticated
    url = reverse('stocks:stock-list')
    response = client.get(url)
    url = reverse('transactions:transaction-list')
    assert response.status_code == 200


