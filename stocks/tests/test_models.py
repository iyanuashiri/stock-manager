import pytest


@pytest.mark.django_db
def test_stock_model(stock, account):

    assert stock.owner == account
    assert stock.name == 'ZOOM'
    assert stock.symbol == 'ZOOM'
    assert stock.unit_price == 50
    assert stock.shares == 1000
    assert stock.total_price == 50000
    assert stock.sell(50, 50) == 950
    assert stock.add_more(100, 50) == 1050


@pytest.mark.django_db
def test_stock_field_label(stock, account):

    assert stock._meta.get_field('owner').verbose_name == 'owner'
    assert stock._meta.get_field('name').verbose_name == 'name'
    assert stock._meta.get_field('symbol').verbose_name == 'symbol'
    assert stock._meta.get_field('unit_price').verbose_name == 'unit price'
    assert stock._meta.get_field('shares').verbose_name == 'shares'
    assert stock._meta.get_field('total_price').verbose_name == 'total price'
    assert stock._meta.get_field('bought_date').verbose_name == 'bought date'


@pytest.mark.django_db
def test_stock_field_attributes(stock):

    assert stock._meta.get_field('name').max_length == 200
    assert stock._meta.get_field('symbol').max_length == 50

