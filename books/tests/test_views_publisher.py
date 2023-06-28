# # pylint:
import json

from _decimal import Decimal
from django.urls import reverse
from rest_framework.test import APITestCase
from snapshottest.django import TestCase
from rest_framework import status

from books.models import Publisher


class PublisherApiTestCase(TestCase):

    def setUp(self):
        self.publisher_1 = Publisher.objects.create(name='Самиздат')

    def test_publisher_get(self):
        url = reverse('publisher-list')
        response = self.client.get(url)
        self.assertMatchSnapshot(response)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_publisher_create(self):
        url = reverse('publisher-list')
        data = {
            "name": "ТестИздат",
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Publisher.objects.all().count(), 2)
        self.assertEqual(Publisher.objects.all()[1].name, 'ТестИздат')

    def test_publisher_update(self):
        url = reverse('publisher-detail', args=(self.publisher_1.id,))
        data = {
            "name": "ТестИздат",
        }
        json_data = json.dumps(data)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Publisher.objects.all()[0].name, 'ТестИздат')

    def test_publisher_delete(self):
        url = reverse('publisher-detail', args=(self.publisher_1.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Publisher.objects.all().count(), 0)
