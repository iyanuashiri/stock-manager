from datetime import datetime

import factory

from accounts.factories import AccountFactory

from .models import Transaction


class TransactionFactory(factory.DjangoModelFactory):

    class Meta:
        model = Transaction

    user = factory.SubFactory(AccountFactory)
    verb = factory.Faker('sentences', nb_words=3)
    created = factory.LazyAttribute(datetime.now())

