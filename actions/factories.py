from datetime import datetime

import factory

from accounts.factories import AccountFactory

from .models import Action


class ActionFactory(factory.DjangoModelFactory):

    class Meta:
        model = Action

    user = factory.SubFactory(AccountFactory)
    verb = factory.Faker('sentences', nb_words=3)
    created = factory.LazyAttribute(datetime.now())

