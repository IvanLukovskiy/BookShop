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

snapshots['AuthorApiTestCase::test_author_get 1'] = [
    {
        'first_name': 'Biba',
        'id': 4,
        'last_name': 'Prigojin',
        'middle_name': 'Lvovich'
    }
]

snapshots['AuthorApiTestCase::test_author_update 1'] = {
    'first_name': 'Biba',
    'id': 5,
    'last_name': 'Leontiev',
    'middle_name': 'Lvovich'
}
