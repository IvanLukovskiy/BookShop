import json
from _decimal import Decimal
from django.urls import reverse
from snapshottest.django import TestCase
from rest_framework import status

from books.models import Books, Author, Publisher


class BooksApiTestCase(TestCase):

    def setUp(self):
        self.author_1 = Author.objects.create(first_name='test_auth', last_name='1', middle_name='2')
        self.publisher_1 = Publisher.objects.create(name='test_pub')
        self.book_1 = Books.objects.create(
            title='test_book',
            price='25.00',
            amount=3,
            publisher=self.publisher_1,
        )
        self.book_1.author.add(self.author_1)

    def test_book_get(self):
        url = reverse('books-list')
        response = self.client.get(url)
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_create(self):
        url = reverse('books-list')
        data = {
            "title": 'Колобок',
            "price": '125.00',
            "amount": 5,
            "author": [1],
            "publisher": 1,
        }
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Books.objects.all()[1].title, 'Колобок')

    def test_book_update(self):
        url = reverse('books-detail', args=(self.book_1.id,))
        data = {
            "title": self.book_1.title,
            "price": '333.00',
            "amount": self.book_1.amount,
            "author": self.book_1.author.all(),
            "publisher": self.publisher_1,
            # "publisher": self.book_1.publisher,
            # "publisher": Publisher.objects.all()[0],
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Books.objects.all()[0].price, Decimal('333.00'))

    def test_book_delete(self):
        url = reverse('books-detail', args=(self.book_1.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Books.objects.all().count(), 0)
