# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['AuthorApiTestCase::test_author_create 1'] = {
    'first_name': 'Author_2',
    'id': 2,
    'last_name': 'Novyi',
    'middle_name': 'Nooone'
}

snapshots['AuthorApiTestCase::test_author_get_list 1'] = [
    {
        'first_name': 'Albert',
        'id': 4,
        'last_name': 'Sysoev',
        'middle_name': 'Valentinovich'
    }
]

snapshots['AuthorApiTestCase::test_author_partial_update 1'] = {
    'first_name': 'Maximus',
    'id': 5,
    'last_name': 'Sysoev',
    'middle_name': 'Valentinovich'
}

snapshots['AuthorApiTestCase::test_author_retrieve_elem 1'] = {
    'first_name': 'Albert',
    'id': 6,
    'last_name': 'Sysoev',
    'middle_name': 'Valentinovich'
}

snapshots['AuthorApiTestCase::test_author_update 1'] = {
    'first_name': 'Albert',
    'id': 7,
    'last_name': 'Leontiev',
    'middle_name': 'Valentinovich'
}
