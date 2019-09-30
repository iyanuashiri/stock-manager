import pytest

from accounts.factories import AccountFactory

from ..factories import TransactionFactory


@pytest.mark.django_db
def test_transaction_model():
    account = AccountFactory()
    transaction = TransactionFactory(user=account, verb='buy')

    assert transaction.user == account


@pytest.mark.django_db
def test_transaction_field_labels():
    account = AccountFactory()
    transaction = TransactionFactory(user=account, verb='buy')

    assert transaction._meta.get_field('user').verbose_name == 'user'
    assert transaction._meta.get_field('verb').verbose_name == 'verb'
    assert transaction._meta.get_field('created').verbose_name == 'created'


@pytest.mark.django_db
def test_transaction_field_attributes():
    account = AccountFactory()
    transaction = TransactionFactory(user=account)

    assert transaction._meta.get_field('verb').max_length == 200
