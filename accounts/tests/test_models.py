import pytest

import factory

from ..factories import AccountFactory


# @pytest.mark.django_db
# def test_account_model():
#     account = AccountFactory()
#
#     assert account.first_name == 'Iyanu'
#     assert account.last_name == 'Iyanu'
#     assert account.email == 'iyanuajao@gmail.com'
#     assert account.get_first_name() == 'Iyanu'
#     assert account.get_fullname() == 'Ajao Iyanu'
#     assert account.email_user('Hey you', 'Hello Iyanu') is True
#

@pytest.mark.django_db
def test_account_label():
    account = AccountFactory()

    assert account._meta.get_field('first_name').verbose_name == 'first name'
    assert account._meta.get_field('last_name').verbose_name == 'last name'
    assert account._meta.get_field('email').verbose_name == 'email address'



@pytest.mark.django_db
def test_account_max_length():
    account = AccountFactory()

    assert account._meta.get_field('first_name').max_length == 200
    assert account._meta.get_field('last_name').max_length == 200
