import pytest

from accounts.factories import AccountFactory
from ..factories import StockFactory


@pytest.mark.django_db
def test_stock_model():
    account = AccountFactory()
    stock = StockFactory(owner=account)

    assert stock.owner == account
    assert stock.name == 'ZOOM'
    assert stock.symbol == 'ZOOM'
    assert stock.unit_price == 50
    assert stock.shares == 1000
    assert stock.total_price == 50000


@pytest.mark.django_db
def test_stock_field_label():
    account = AccountFactory()
    stock = StockFactory(owner=account)

    assert stock._meta.get_field('owner').verbose_name == 'owner'
    assert stock._meta.get_field('name').verbose_name == 'name'
    assert stock._meta.get_field('symbol').verbose_name == 'symbol'
    assert stock._meta.get_field('unit_price').verbose_name == 'unit price'
    assert stock._meta.get_field('shares').verbose_name == 'shares'
    assert stock._meta.get_field('total_price').verbose_name == 'total price'
    assert stock._meta.get_field('bought_date').verbose_name == 'bought date'


@pytest.mark.django_db
def test_stock_field_attributes():
    account = AccountFactory()
    stock = StockFactory(owner=account)

    assert stock._meta.get_field('name').max_length == 200
    assert stock._meta.get_field('symbol').max_length == 50

