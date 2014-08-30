import os
import unittest
import tempfile
from nose.tools import *
from app import app
from gothonweb.tests.tools import assert_response

app.config['TESTING'] = True
test_app = app.test_client()

def test_index():
    # check that we get a 404 on the /hello URL
    resp = test_app.get("/hello")
    assert_response(resp, status='404')

    # test our first GET request to /
    resp = test_app.get('/')
    assert_response(resp, status='302')

    # test our first GET request to /game
    resp = test_app.get('/game')
    assert_response(resp, status='200')

    # make sure default values work for the form
    resp = test_app.post('/game')
    assert_response(resp, status='302')

    # test that we get expected values
    data = {'action': 'tell a joke!'}
    resp = test_app.post('/game', data=data)
    assert_response(resp, status='302')


# class GothonWebTestCase(unittest.TestCase):
#     def setUp(self):
#         app.app.config['TESTING'] = True
#         self.app = app.app.test_client()

#     def tearDown(self):
#         pass

# if __name__ == '__main__':
#     unittest.main()
