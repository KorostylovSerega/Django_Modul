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

    def test_form_valid(self):
        form = UserCreateForm(data={'username': 'simple',
                                    'email': 'simplecustomer@gmail.com',
                                    'password1': 'simplepassword',
                                    'password2': 'simplepassword',
                                    'deposit': 2000})
        self.assertTrue(form.is_valid())
        request = RequestFactory().post(reverse('register'))
        request.session = SessionStore()
        request.user = AnonymousUser()
        print(request.user)
        view = UserCreateView()
        view.setup(request)
        view.form_valid(form)
        print(request.user)
        self.assertTrue(request.user.is_authenticated)


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

