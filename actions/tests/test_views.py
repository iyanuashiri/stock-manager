from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

import pytest


class TestActionList(APITestCase):

    @pytest.mark.django_db
    def test_can_get_action_list(self):
        url = reverse('action-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


