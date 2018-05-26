from django.test import TestCase,Client
from django.urls import resolve
from django.http import HttpRequest
from django.core.urlresolvers import reverse
from calc_fibonacci.views import index,result

#  Test for the views before functionality development
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

# Test to see home page or landing page has some valid HTML
    def test_home_page_returns_correct_html(self):
            request = HttpRequest()
            response = index(request)
            html = response.content.decode('utf8')
            self.assertTrue(html.startswith('<html>'))
            self.assertIn('<title>Fibonacci Generator</title>', html)
            self.assertTrue(html.endswith('</html>'))
            
# Now test for the views after functionality development
class GetTest(TestCase):
    def setUp(self):
        self.client = Client()
    def test_getLogin(self):
        self.response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)
class ExapmplePostTest(TestCase):
    def setUp(self):
        self.client = Client()
    def test_addAccount(self):
        data='10'
        response = self.client.post('/result',{'input':data})
        self.assertEqual(response.status_code, 200)
