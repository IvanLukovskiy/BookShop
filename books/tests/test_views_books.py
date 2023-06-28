# pylint: disable=no-member
import json

from _decimal import Decimal
from django.urls import reverse
from rest_framework.test import APITestCase
from snapshottest.django import TestCase
from rest_framework import status

from books.models import Books, Author, Publisher


class BooksApiTestCase(TestCase):
    #
    # def setUp(self):
    #     self.book_1 = Books.objects.create(title='test_book', price='25.00', amount=3)
    #     self.author_1 = Author.objects.create(first_name='test_auth', last_name='1', middle_name='2')
    #     self.publisher_1 = Publisher.objects.create(name='test_pub')

    def test_book_get(self):
        url = reverse('books-list')
        response = self.client.get(url)
        self.assertMatchSnapshot(response)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertMatchSnapshot(response.json())

#     def test_book_create(self):
#         url = reverse('books-list')
#         data = {
#             "title": 'Колобок',
#             "price": '125.00',
#             "amount": 5,
#             "author": [1],
#             "publisher": 1 ,
#         }
#         json_data = json.dumps(data)
#         response = self.client.post(url, data=json_data, content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Books.objects.all()[0].title, 'Колобок')

    # def test_book_update(self):
    #     url = reverse('books-detail', args=(self.book_1.id,))
    #     data = {
    #         "title": self.book_1.title,
    #         "price": '333.00',
    #         "amount": self.book_1.amount,
    #     }
    #     json_data = json.dumps(data)
    #     response = self.client.put(url, data=json_data, content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(Books.objects.all()[0].price, Decimal('333.00'))
    #
    # def test_book_delete(self):
    #     url = reverse('books-detail', args=(self.book_1.id,))
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, 204)
    #     self.assertEqual(Books.objects.all().count(), 1)
