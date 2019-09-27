import pytest

from accounts.factories import AccountFactory

from ..factories import TransactionFactory


@pytest.mark.django_db
def test_action_model():
    account = AccountFactory()
    action = TransactionFactory(user=account)

    assert action.user == TransactionFactory.user
    assert action.verb == TransactionFactory.verb
    assert action.created == TransactionFactory.created


@pytest.mark.django_db
def test_action_field_labels():
    account = AccountFactory()
    action = TransactionFactory(user=account)

    assert action._meta.get_field('user') == 'user'
    assert action._meta.get_field('verb') == 'verb'
    assert action._meta.get_field('created') == 'created'


@pytest.mark.django_db
def test_action_field_attributes():
    account = AccountFactory()
    action = TransactionFactory(user=account)

    assert action._meta.get_field('verb').max_length == 200
