# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['PublisherApiTestCase::test_publisher_create 1'] = {
    'id': 6,
    'name': 'ТестИздат'
}

snapshots['PublisherApiTestCase::test_publisher_get 1'] = [
    {
        'id': 8,
        'name': 'Самиздат'
    }
]

snapshots['PublisherApiTestCase::test_publisher_update 1'] = {
    'id': 9,
    'name': 'ТестИздат'
}
