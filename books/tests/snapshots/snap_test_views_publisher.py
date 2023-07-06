# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['PublisherApiTestCase::test_publisher_create 1'] = {
    'id': 8,
    'name': 'ТестИздат'
}

snapshots['PublisherApiTestCase::test_publisher_get_list 1'] = [
    {
        'id': 10,
        'name': 'test_pub'
    }
]

snapshots['PublisherApiTestCase::test_publisher_partial_update 1'] = {
    'id': 11,
    'name': 'ТестИздат'
}

snapshots['PublisherApiTestCase::test_publisher_retrieve_elem 1'] = {
    'id': 12,
    'name': 'test_pub'
}

snapshots['PublisherApiTestCase::test_publisher_update 1'] = {
    'id': 13,
    'name': 'ТестИздат'
}
