from _decimal import Decimal
from django.urls import reverse
from snapshottest.django import TestCase
from rest_framework import status
from freezegun import freeze_time

from books.models import Books
from books.factories import BooksFactory, PublisherFactory, AuthorFactory


@freeze_time("2023-07-25  01:02:00")
class BooksApiTestCase(TestCase):
    def setUp(self):
        self.publisher_1 = PublisherFactory()

        self.author_1 = AuthorFactory.create()

        self.book_1 = BooksFactory(title='setup_book_1',
                                   price='25.00',
                                   amount=76,
                                   author=(self.author_1,),
                                   publisher=self.publisher_1
                                   )

    def test_book_get_list(self):
        url = reverse('books-list')
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Books.objects.all().count(), 1)
        self.assertMatchSnapshot(response.json())

    def test_book_get_retrieve_elem(self):
        url = reverse('books-detail', args=(self.book_1.id,))
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Books.objects.all().count(), 1)
        self.assertMatchSnapshot(response.json())

    def test_book_create(self):
        url = reverse('books-list')
        book_inst = Books.objects.get(title='setup_book_1')
        data = {
            "title": 'Колобок',
            "price": '125.00',
            "amount": 5,
            "author": [book_inst.author.get(first_name='Albert').id],
            "publisher": self.book_1.publisher.id,
        }
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Books.objects.all()[1].title, 'Колобок')

    def test_book_update(self):
        url = reverse('books-detail', args=(self.book_1.id,))
        book_inst = Books.objects.get(title='setup_book_1')
        data = {
            "title": self.book_1.title,
            "price": '333.00',
            "amount": self.book_1.amount,
            # "author": self.book_1.author_set.all(),
            "author": [book_inst.author.get(first_name='Albert').id],
            "publisher": self.book_1.publisher.id,
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Books.objects.all()[0].price, Decimal('333.00'))

    def test_book_partial_update(self):
        url = reverse('books-detail', args=(self.book_1.id,))
        book_inst = Books.objects.get(title='setup_book_1')
        data = {
            "title": self.book_1.title,
            "price": '226.00',
            "author": [book_inst.author.get(first_name='Albert').id],
            "publisher": self.book_1.publisher.id,
        }
        response = self.client.patch(url, data=data, content_type='application/json')
        self.assertMatchSnapshot(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Books.objects.all()[0].price, Decimal('226.00'))

    def test_book_delete(self):
        url = reverse('books-detail', args=(self.book_1.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Books.objects.all().count(), 0)
