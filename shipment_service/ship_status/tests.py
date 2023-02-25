from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ship_status.models import Shipment
import json


class ShipmentTests(APITestCase):

    def post_shipment(self, fname, lname, email, mobile, address, product_id, quantity, payment_status, transaction_id):
        url = reverse('shipment_reg_update')

        data = {
            'fname': fname, 'lname': lname, 'email': email,
            'mobile': mobile, 'address': address, 'product_id': product_id,
            'quantity': quantity, 'payment_status': payment_status,
            'transaction_id': transaction_id
        }
        response = self.client.post(url, data, format='json')
        return json.loads(response.content)

    def shipment_status(self, email):
        url = reverse('shipment_status')
        data = {
         'email': email,
        }
        response = self.client.post(url, data, format='json')
        return json.loads(response.content)
  

    def test_shipment_post_and_retrieve(self):
        fname = "Andre"
        lname = "Hangalo"
        email = "hangaloandre@gmail.com"
        mobile = "940171369"
        address = "Huila, Lubango"
        product_id = "01"
        quantity = "2"
        payment_status = "01"
        transaction_id = "02"

        response = self.post_shipment(
            fname, lname, email, mobile, 
            address, product_id, quantity, 
            payment_status,transaction_id
            )
        print(f"Print value response: {response}")

        assert response['status_code'] == status.HTTP_200_OK
        assert Shipment.objects.get().fname == fname

    def test_shipment_get_data(self):
 
        fname = "Andre"
        lname = "Hangalo"
        email = "hangaloandre@gmail.com"
        mobile = "940171369"
        address = "Huila, Lubango"
        product_id = "01"
        quantity = "2"
        payment_status = "01"
        transaction_id = "02"

        response = self.post_shipment(
            fname, lname, email, mobile, 
            address, product_id, quantity, 
            payment_status,transaction_id
            )
        print(f"Print value response: {response}")

        assert response['status_code'] == status.HTTP_200_OK
        assert Shipment.objects.get().fname == fname

        email1 = 'hangaloandre@gmail.com'

        response1 = self.shipment_status(email1)
        print(f"Print value response1: {response1}")

        assert response1['status_code'] == status.HTTP_200_OK
        assert response1['message']['email'] == email1

    def test_shipment_get_data_user_none_exists(self):
 
        fname = "Andre"
        lname = "Hangalo"
        email = "hangaloandre@gmail.com"
        mobile = "940171369"
        address = "Huila, Lubango"
        product_id = "01"
        quantity = "2"
        payment_status = "01"
        transaction_id = "02"

        response = self.post_shipment(
            fname, lname, email, mobile, 
            address, product_id, quantity, 
            payment_status,transaction_id
            )
        print(f"Print value response: {response}")

        assert response['status_code'] == status.HTTP_200_OK
        assert Shipment.objects.get().fname == fname

        email1 = 'email@noneexist.com'

        response1 = self.shipment_status(email1)
        print(f"Print value response1: {response1}")

        assert response1['status_code'] == status.HTTP_400_BAD_REQUEST
