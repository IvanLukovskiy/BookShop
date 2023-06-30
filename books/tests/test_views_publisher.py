import json

from _decimal import Decimal
from django.urls import reverse
from snapshottest.django import TestCase
from rest_framework import status

from books.models import Publisher


class PublisherApiTestCase(TestCase):

    def setUp(self):
        self.publisher_1 = Publisher.objects.create(name='Самиздат')

    def test_publisher_get(self):
        url = reverse('publisher-list')
        response = self.client.get(url)
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_publisher_create(self):
        url = reverse('publisher-list')
        data = {
            "name": "ТестИздат",
        }
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Publisher.objects.all().count(), 2)
        self.assertEqual(Publisher.objects.all()[1].name, 'ТестИздат')

    def test_publisher_update(self):
        url = reverse('publisher-detail', args=(self.publisher_1.id,))
        data = {
            "name": "ТестИздат",
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Publisher.objects.all()[0].name, 'ТестИздат')

    def test_publisher_delete(self):
        url = reverse('publisher-detail', args=(self.publisher_1.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Publisher.objects.all().count(), 0)
