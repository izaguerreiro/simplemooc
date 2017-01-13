from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class ContactViewTests(TestCase):
    def setUp(self):
        client = Client()
        self.response = client.get(reverse('core:contact'))

    def test_home_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_template_used(self):
        self.assertTemplateUsed(self.response, 'contact.html')
        self.assertTemplateUsed(self.response, 'base.html')