from django.test import TestCase
from django.test import Client
from ..forms import BreweriesForm

class BreweriesFormTest(TestCase):

    def test_brewery_form_valid(self):
        form = BreweriesForm(data={'latitude': 51.49999, 'longitude': 25.4555})
        self.assertTrue(form.is_valid())

    def test_brewery_form_invalid(self):
        form = BreweriesForm(data={'latitude': '', 'longitude': ''})
        self.assertFalse(form.is_valid())