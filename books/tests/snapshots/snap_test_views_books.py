# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['BooksApiTestCase::test_book_create 1'] = {
    'amount': 5,
    'author': [
        6
    ],
    'id': 2,
    'price': '125.00',
    'publisher': 1,
    'time_create': '2023-07-03T09:25:51.778364+03:00',
    'time_update': '2023-07-03T09:25:51.778364+03:00',
    'title': 'Колобок'
}

snapshots['BooksApiTestCase::test_book_get 1'] = [
    {
        'amount': 76,
        'author': [
            8
        ],
        'id': 4,
        'price': '25.00',
        'publisher': 3,
        'time_create': '2023-07-03T09:25:51.826379+03:00',
        'time_update': '2023-07-03T09:25:51.829385+03:00',
        'title': 'setup_book_1'
    }
]

snapshots['BooksApiTestCase::test_book_update 1'] = {
    'amount': 76,
    'author': [
        9
    ],
    'id': 5,
    'price': '333.00',
    'publisher': 4,
    'time_create': '2023-07-03T09:25:51.850415+03:00',
    'time_update': '2023-07-03T09:25:51.872378+03:00',
    'title': 'setup_book_1'
}
