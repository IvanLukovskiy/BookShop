# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['BooksApiTestCase::test_book_create 1'] = {
    'author': [
        'Недопустимый первичный ключ "1" - объект не существует.'
    ]
}

snapshots['BooksApiTestCase::test_book_get 1'] = [
    {
        'amount': 3,
        'author': [
            8
        ],
        'id': 3,
        'price': '25.00',
        'publisher': 3,
        'time_create': '2023-06-30T09:27:01.777670+03:00',
        'time_update': '2023-06-30T09:27:01.777670+03:00',
        'title': 'test_book'
    }
]
