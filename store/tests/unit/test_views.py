from django.contrib.auth import authenticate, login
from django.test import TestCase, RequestFactory
from django.urls import reverse

from store.models import MyUser
from store.views import UserCreateView


class UserCreateViewTestCase(TestCase):

    def setUp(self):
        self.form_data = {
            'username': 'simple',
            'password': 'simple-password'
        }
        MyUser.objects.create_user(username=self.form_data.get('username'),
                                   password=self.form_data.get('password'))

    def test_form_valid_is_makes_login(self):
        username = self.form_data.get('username')
        password = self.form_data.get('password')
        user = authenticate(username=username,
                            password=password)
        self.assertTrue(user.is_authenticated)


class PurchaseListViewTestCase(TestCase):
    pass


class PurchaseCreateViewTestCase(TestCase):
    pass


class ReturnListViewTestCase(TestCase):
    pass


class ReturnCreateViewTestCase(TestCase):
    pass


class PurchaseDeleteViewTestCase(TestCase):
    pass

