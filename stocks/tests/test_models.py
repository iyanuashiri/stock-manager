import pytest

from accounts.factories import AccountFactory
from ..factories import StockFactory


@pytest.mark.django_db
def test_stock_model():
    account = AccountFactory()
    stock = StockFactory(owner=account)

    assert stock.owner == StockFactory.owner
    assert stock.name == StockFactory.name
    assert stock.symbol == StockFactory.symbol
    assert stock.unit_price == StockFactory.unit_price
    assert stock.shares == StockFactory.shares
    assert stock.total_price == StockFactory.total_price
    assert stock.bought_date == StockFactory.bought_date


@pytest.mark.django_db
def test_stock_field_label():
    account = AccountFactory()
    stock = StockFactory(owner=account)

    assert stock._meta.get_field('owner') == 'owner'
    assert stock._meta.get_field('name') == 'name'
    assert stock._meta.get_field('symbol') == 'symbol'
    assert stock._meta.get_field('unit_price') == 'unit_price'
    assert stock._meta.get_field('shares') == 'shares'
    assert stock._meta.get_field('total_price') == 'total_price'
    assert stock._meta.get_field('bought_date') == 'bought_date'


@pytest.mark.django_db
def test_stock_field_attributes():
    account = AccountFactory()
    stock = StockFactory(owner=account)

    assert stock._meta.get_field('name').max_length == 200
    assert stock._meta.get_field('symbol').max_length == 50

    assert stock._meta.get_field('owner').related_name == 'stocks'
