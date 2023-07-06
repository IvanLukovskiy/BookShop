from django.urls import reverse
from snapshottest.django import TestCase
from rest_framework import status

from books.models import Author
from books.factories import AuthorFactory


class AuthorApiTestCase(TestCase):

    def setUp(self):
        self.author_1 = AuthorFactory()

    def test_author_get_list(self):
        url = reverse('author-list')
        response = self.client.get(url)
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_retrieve_elem(self):
        url = reverse('author-detail', args=(self.author_1.id,))
        response = self.client.get(url)
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_create(self):
        url = reverse('author-list')
        data = {
            "first_name": "Author_2",
            "last_name": "Novyi",
            "middle_name": "Nooone"
        }
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.all().count(), 2)
        self.assertEqual(Author.objects.all()[1].first_name, 'Author_2')

    def test_author_update(self):
        url = reverse('author-detail', args=(self.author_1.id,))
        data = {
            "first_name": self.author_1.first_name,
            "last_name": 'Leontiev',
            "middle_name": self.author_1.middle_name,
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.all()[0].last_name, 'Leontiev')

    def test_author_partial_update(self):
        url = reverse('author-detail', args=(self.author_1.id,))
        data = {
            "first_name": "Maximus",
        }
        response = self.client.patch(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.all()[0].first_name, 'Maximus')

    def test_author_delete(self):
        url = reverse('author-detail', args=(self.author_1.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.all().count(), 0)
