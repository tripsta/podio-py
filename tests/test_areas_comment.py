#!/usr/bin/env python
"""
Unit tests for pypodio2.areas.Comment (via pypodio2.client.Client). Works
by mocking httplib2, and making assertions about how pypodio2 calls
it.
"""

try:
    import json
except ImportError:
    import simplejson as json

from mock import Mock
from nose.tools import eq_

from tests.utils import check_client_method, get_client_and_http, URL_BASE

def test_create():

	commentable_type = 'item'
	commentable_id = 1

	attributes = {'value': '[rnd/bugs-1]', 'external-id' : '045e620f7be09630a16288a145a3e54d0c9a254b'}

	client, check_assertions = check_client_method()
	result = client.Comment.create(commentable_type, commentable_id, attributes)
	check_assertions(result,
					'POST',
					'/comment/%s/%d' % (commentable_type, commentable_id),
					json.dumps(attributes),
					{'content-type': 'application/json'})