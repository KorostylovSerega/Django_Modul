from django.test import TestCase, RequestFactory
from django.urls import reverse

from store.models import MyUser
from store.views import UserCreateView


class UserCreateViewTestCase(TestCase):

    def test_page_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'registration/registration.html')

    def test_page_incorrect_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateNotUsed(response, 'registration/login.html')

    def test_form_valid_is_makes_login(self):
        user = MyUser.objects.create_user(username='test',
                                          password='example-password')
        self.assertTrue(user.is_authenticated)


class ProductListViewTestCase(TestCase):

    def test_page_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'store/home.html')

    def test_page_incorrect_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateNotUsed(response, 'store/purchase.html')


class ProductCreateViewTestCase(TestCase):
    pass


class ProductUpdateViewTestCase(TestCase):
    pass


class PurchaseListViewTestCase(TestCase):
    pass


class PurchaseCreateViewTestCase(TestCase):
    pass


class ReturnListViewTestCase(TestCase):
    pass


class ReturnCreateViewTestCase(TestCase):
    pass


class ReturnDeleteViewTestCase(TestCase):
    pass


class PurchaseDeleteViewTestCase(TestCase):
    pass

