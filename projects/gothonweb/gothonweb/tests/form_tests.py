import os
import unittest
import tempfile
from nose.tools import *
from app_hello import app
from gothonweb.tests.tools import assert_response

app.config['TESTING'] = True
test_app = app.test_client()

def test_index():
    # check that we get a 404 on the / URL
    resp = test_app.get("/")
    assert_response(resp, status='404')

    # test our first GET request to /hello
    resp = test_app.get('/hello')
    assert_response(resp)

    # make sure default values work for the form
    resp = test_app.post('/hello')
    assert_response(resp, contains="Nobody")

    # test that we get expected values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = test_app.post('/hello', data=data)
    assert_response(resp, contains='Zed')


# class GothonWebTestCase(unittest.TestCase):
#     def setUp(self):
#         app.app.config['TESTING'] = True
#         self.app = app.app.test_client()

#     def tearDown(self):
#         pass

# if __name__ == '__main__':
#     unittest.main()
