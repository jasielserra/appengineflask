# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest

@pytest.fixture
def home_resp(test_client):
    resp = test_client.get('/')
    return resp

def test_status_code(home_resp):
    assert 200 == home_resp.status_code

def test_subscription_link(home_resp):
    assert '/inscricao/' in home_resp.data.decode('utf8')


'''
def test_content():
    client = app.test_client()
    resp = client.get('/')
    assert 'Inscreva-se' == resp.data
'''