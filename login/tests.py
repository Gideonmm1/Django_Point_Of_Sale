from urllib import response
from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)