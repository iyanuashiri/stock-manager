from django.urls import reverse

import pytest


@pytest.mark.django_db
def test_stock_list(authenticated):
    client = authenticated
    url = reverse('stocks:stock-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_stock_buy(authenticated):
    client = authenticated
    url = reverse('stocks:stock-buy', kwargs={'symbol': 'ZOOM', 'shares': 1000})
    response = client.post(url)
    assert response.status_code == 201


@pytest.mark.django_db
def test_stock_sell(authenticated, stock):
    client = authenticated
    url = reverse('stocks:stock-sell', kwargs={'symbol': 'ZOOM', 'shares': 100})
    response = client.put(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_stock_search(authenticated):
    client = authenticated
    url = reverse('stocks:stock-search', kwargs={'symbol': 'ZOOM'})
    response = client.get(url)
    assert response.status_code == 200