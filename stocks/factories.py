from datetime import datetime

import factory

from accounts.factories import AccountFactory

from .models import Stock


class StockFactory(factory.DjangoModelFactory):

    class Meta:
        model = Stock

    owner = factory.SubFactory(AccountFactory)
    name = 'ZOOM'
    symbol = 'ZOOM'
    unit_price = 50
    shares = 1000
    total_price = factory.LazyAttribute(lambda a: a.unit_price*a.shares)
    bought_date = factory.LazyFunction(datetime.now)
