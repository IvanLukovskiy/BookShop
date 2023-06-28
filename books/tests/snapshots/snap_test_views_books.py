# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['BooksApiTestCase::test_book_get 1'] = GenericRepr('<Response status_code=200, "application/json">')
