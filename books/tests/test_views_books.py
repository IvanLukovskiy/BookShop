import json
from _decimal import Decimal
from django.urls import reverse
from snapshottest.django import TestCase
from rest_framework import status

from books.models import Books
from books.tests.books_factory import BooksFactory, PublisherFactory, AuthorFactory


class BooksApiTestCase(TestCase):
    def setUp(self):
        self.publisher_1 = PublisherFactory(name='test_pub')

        self.author_1 = AuthorFactory.create(first_name='Albert',
                                             last_name='Sysoev',
                                             middle_name='Valentinovich')

        self.book_1 = BooksFactory(title='setup_book_1',
                                   price='25.00',
                                   amount=76,
                                   author=(self.author_1,),
                                   publisher=self.publisher_1
                                   )

    def test_book_get(self):
        url = reverse('books-list')
        data = {
            "title": 'setup_book',
            "price": '25.00',
            "amount": 70,
            "author": [1],
            "publisher": 1,
        }
        response = self.client.get(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_book_create(self):
        url = reverse('books-list')
        z = Books.objects.get(title='setup_book_1')
        data = {
            "title": 'Колобок',
            "price": '125.00',
            "amount": 5,
            "author": [z.author.get(first_name='Albert').id],
            "publisher": self.book_1.publisher.id,
        }
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Books.objects.all()[1].title, 'Колобок')

    def test_book_update(self):
        url = reverse('books-detail', args=(self.book_1.id,))
        z = Books.objects.get(title='setup_book_1')
        data = {
            "title": self.book_1.title,
            "price": '333.00',
            "amount": self.book_1.amount,
            "author": [z.author.get(first_name='Albert').id],
            "publisher": self.book_1.publisher.id,
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
