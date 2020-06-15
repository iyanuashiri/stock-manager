import pytest


@pytest.mark.django_db
def test_transaction_model(transaction, account):

    assert transaction.user == account


@pytest.mark.django_db
def test_transaction_field_labels(transaction):

    assert transaction._meta.get_field('user').verbose_name == 'user'
    assert transaction._meta.get_field('verb').verbose_name == 'verb'
    assert transaction._meta.get_field('created').verbose_name == 'created'


@pytest.mark.django_db
def test_transaction_field_attributes(account, transaction):
    assert transaction._meta.get_field('verb').max_length == 200
