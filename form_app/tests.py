from django.test import Client, TestCase

from .models import product


class ProductFormViewTests(TestCase):
    def test_create_product_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Product')

    def test_create_product_form_saves_product(self):
        response = self.client.post('/', {
            'name': 'Laptop',
            'description': 'Gaming laptop',
            'price': '999.99',
            'is_available': 'True',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(product.objects.filter(name='Laptop').exists())

    def test_product_details_page_displays_product(self):
        item = product.objects.create(
            name='Laptop',
            description='Gaming laptop',
            price='999.99',
            is_available=True,
        )

        response = self.client.get(f'/products/{item.pk}/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')
        self.assertContains(response, 'Gaming laptop')
        self.assertContains(response, '999.99')

    def test_product_details_page_returns_404_for_missing_product(self):
        response = self.client.get('/products/99999/')

        self.assertEqual(response.status_code, 404)

    def test_product_search_page_loads(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product Search')

    def test_product_search_finds_matching_products(self):
        product.objects.create(name='Wireless Mouse', price='29.99')
        product.objects.create(name='Mechanical Keyboard', price='79.99')

        response = self.client.get('/search/', {'query': 'mouse'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wireless Mouse')
        self.assertNotContains(response, 'Mechanical Keyboard')
