from django.contrib.auth import authenticate, login
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from store.forms import UserCreateForm
from store.models import MyUser
from store.views import UserCreateView


class UserCreateViewTestCase(TestCase):

    def setUp(self):
        self.form = UserCreateForm(data={'username': 'simple',
                                         'email': 'simplecustomer@gmail.com',
                                         'password1': 'simplepassword',
                                         'password2': 'simplepassword',
                                         'deposit': 2000})
        self.request = RequestFactory().post(reverse('register'))
        self.view = UserCreateView()

    def test_form_valid_create_user(self):
        self.request.session = SessionStore()
        self.request.user = AnonymousUser()
        self.view.setup(self.request)
        self.view.form_valid(self.form)
        user = MyUser.objects.get(email='simplecustomer@gmail.com')
        self.assertEqual(user.username, 'simple')

    def test_form_valid_authenticate_user(self):
        self.request.session = SessionStore()
        self.request.user = AnonymousUser()
        self.view.setup(self.request)
        self.view.form_valid(self.form)
        self.assertTrue(self.request.user.is_authenticated)


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
