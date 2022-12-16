from django.test import TestCase

from store.models import Product, MyUser, Purchase, ReturnPurchase


class ProductTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(title='test_title',
                                              description='test_description',
                                              price=2000,
                                              quantity=1)

    def test_product_name_is_title(self):
        self.assertEqual(self.product.title, str(self.product))


class PurchaseTestCase(TestCase):

    customer = None
    product = None
    purchase = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.customer = MyUser.objects.create_user(username='test',
                                                  password='example-password')
        cls.product = Product.objects.create(title='test_title',
                                             description='test_description',
                                             price=2000,
                                             quantity=5)
        cls.purchase = Purchase.objects.create(customer=cls.customer,
                                               product=cls.product,
                                               quantity=3)

    def test_purchase_name_is_product_name(self):
        self.assertEqual(str(PurchaseTestCase.product), str(PurchaseTestCase.purchase))

    def test_purchase_amount_property(self):
        purchase_amount = PurchaseTestCase.product.price * PurchaseTestCase.purchase.quantity
        self.assertEqual(PurchaseTestCase.purchase.purchase_amount, purchase_amount)


class ReturnPurchaseTestCase(TestCase):

    def setUp(self):
        self.customer = MyUser.objects.create_user(username='test',
                                                   password='example-password')
        self.product = Product.objects.create(title='test_title',
                                              description='test_description',
                                              price=200,
                                              quantity=3)
        self.purchase = Purchase.objects.create(customer=self.customer,
                                                product=self.product,
                                                quantity=1)
        self.purchase_return = ReturnPurchase.objects.create(purchase=self.purchase)

    def test_return_name_is_purchase_name(self):
        self.assertEqual(str(self.purchase), str(self.purchase_return))
