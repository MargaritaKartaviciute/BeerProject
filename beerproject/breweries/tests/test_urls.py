from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import BreweriesView

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class, BreweriesView)
