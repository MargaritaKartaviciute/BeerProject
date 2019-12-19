from django.test import TestCase, Client
from django.urls import reverse

import json
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.csrf_client = Client(enforce_csrf_checks=True)
        self.template_name = 'index.html'

    def test_breweries_view(self):
        response = self.client.get("/breweries/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)

    def test_breweries_post_without_csrf_token_check(self):

        response = self.client.post("/breweries/", {'latitude': 51.7555, 'longitude': 66.55555})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)

    def test_breweries_post_with_csrf_token_check(self):

        response = self.csrf_client.post("/breweries/", {'latitude': 51.7555, 'longitude': 66.55555})
        self.assertEqual(response.status_code, 403)
