from datetime import datetime

import factory

from accounts.factories import AccountFactory

from .models import Stock


class StockFactory(factory.DjangoModelFactory):

    class Meta:
        model = Stock

    owner = factory.SubFactory(AccountFactory)
    name = factory.Faker('name')
    symbol = factory.Faker('name')
    unit_price = factory.Faker('number')
    shares = factory.Faker('number')
    total_price = factory.LazyAttribute(lambda a: f'{a.unit_price}*{a.shares}')
    bought_date = factory.LazyFunction(datetime.now)
