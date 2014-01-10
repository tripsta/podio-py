#!/usr/bin/env python
"""
Unit tests for pypodio2.areas.Application (via pypodio2.client.Client). Works
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

def test_find_by_org_space_and_app_labels():
	org_label = 'travelplanet24com'
	space_label = 'rnd-team'
	app_label = 'stories'

	client, check_assertions = check_client_method()
	result = client.Application.find_by_org_space_and_app_labels(org_label, space_label, app_label)
	check_assertions(result, 'GET', '/app/org/%s/space/%s/%s' % (org_label, space_label, app_label))