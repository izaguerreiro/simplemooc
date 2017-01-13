from django.test import TestCase
from django.core import mail
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings
from simplemooc.courses.models import Course


class ContactCourse(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Django', slug='django')

    def tearDown(self):
        self.course.delete()

    def test_contact_from_error(self):
        data = {'name': 'Fulano', 'email': '', 'message': ''}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def test_contact_form_success(self):
        data = {'name': 'Fulano', 'email': 'fulano@fulano.com', 'message': 'Dúvidas'}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])