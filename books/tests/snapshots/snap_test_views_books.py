# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['BooksApiTestCase::test_book_create 1'] = {
    'amount': 5,
    'author': [
        8
    ],
    'id': 2,
    'price': '125.00',
    'publisher': 1,
    'time_create': '2023-07-25T04:02:00+03:00',
    'time_update': '2023-07-25T04:02:00+03:00',
    'title': 'Колобок'
}

snapshots['BooksApiTestCase::test_book_get_list 1'] = [
    {
        'amount': 76,
        'author': [
            10
        ],
        'id': 4,
        'price': '25.00',
        'publisher': 3,
        'time_create': '2023-07-25T04:02:00+03:00',
        'time_update': '2023-07-25T04:02:00+03:00',
        'title': 'setup_book_1'
    }
]

snapshots['BooksApiTestCase::test_book_get_retrieve_elem 1'] = {
    'amount': 76,
    'author': [
        11
    ],
    'id': 5,
    'price': '25.00',
    'publisher': 4,
    'time_create': '2023-07-25T04:02:00+03:00',
    'time_update': '2023-07-25T04:02:00+03:00',
    'title': 'setup_book_1'
}

snapshots['BooksApiTestCase::test_book_partial_update 1'] = {
    'amount': 76,
    'author': [
        12
    ],
    'id': 6,
    'price': '226.00',
    'publisher': 5,
    'time_create': '2023-07-25T04:02:00+03:00',
    'time_update': '2023-07-25T04:02:00+03:00',
    'title': 'setup_book_1'
}

snapshots['BooksApiTestCase::test_book_update 1'] = {
    'amount': 76,
    'author': [
        13
    ],
    'id': 7,
    'price': '333.00',
    'publisher': 6,
    'time_create': '2023-07-25T04:02:00+03:00',
    'time_update': '2023-07-25T04:02:00+03:00',
    'title': 'setup_book_1'
}
