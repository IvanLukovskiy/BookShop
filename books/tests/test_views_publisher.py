from django.urls import reverse
from snapshottest.django import TestCase
from rest_framework import status

from books.models import Publisher
from books.factories import PublisherFactory


class PublisherApiTestCase(TestCase):

    def setUp(self):
        self.publisher_1 = PublisherFactory()

    def test_publisher_get_list(self):
        url = reverse('publisher-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_publisher_retrieve_elem(self):
        url = reverse('publisher-detail', args=(self.publisher_1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_publisher_create(self):
        url = reverse('publisher-list')
        data = {
            "name": "ТестИздат",
        }
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertMatchSnapshot(response.json())

    def test_publisher_update(self):
        url = reverse('publisher-detail', args=(self.publisher_1.id,))
        data = {
            "name": "ТестИздат",
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_publisher_partial_update(self):
        url = reverse('publisher-detail', args=(self.publisher_1.id,))
        data = {
            "name": "ТестИздат",
        }
        response = self.client.patch(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_publisher_delete(self):
        url = reverse('publisher-detail', args=(self.publisher_1.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
