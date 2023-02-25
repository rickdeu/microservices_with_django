from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from product_model.models import ProductDetails
import json


class ProductModelTests(APITestCase):

    def post_product(self, product_id, product_category, product_name, availability, price):
        url = reverse('get_product_data')
        data = {
            "product_id": product_id, "product_category": product_category,
            "product_name": product_category, "availability": availability, "price": price
        }
        response = self.client.post(url, data, format="json")
        return response

    def test_product_post_and_retrieve(self):
        product_id, product_category, product_name, availability, price = "01", "Water", "Chela Water", "1", "200"
        response = self.post_product(product_id, product_category, product_name, availability, price)

        data = json.loads(response.content)
