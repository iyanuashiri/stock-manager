from datetime import datetime

from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType

import factory

from accounts.factories import AccountFactory

from .models import Transaction


class TransactionFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(AccountFactory)
    target_id = factory.SelfAttribute('target.id')
    target = factory.SubFactory(AccountFactory)
    target_ct = factory.LazyAttribute(lambda o: ContentType.objects.get_for_model(o.target))
    created = factory.LazyFunction(datetime.now)

    class Meta:
        # exclude = ['target']
        model = Transaction


# class GroupFactory(factory.django.DjangoModelFactory):
#     name = 'group'
#
#     class Meta:
#         model = Group
#
#
# class TransactionUserFactory(TransactionFactory):
#     target = factory.SubFactory(AccountFactory)
#
#     class Meta:
#         model = Transaction
#
#
# class TransactionGroupFactory(TransactionFactory):
#     target = factory.SubFactory(GroupFactory)
#
#     class Meta:
#         model = Transaction
#
#
#
#
#
#
