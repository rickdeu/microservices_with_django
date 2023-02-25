
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user_model.models import UserRegistration
import json

class UserRegistrationTests(APITestCase):

    def post_user_regirstration(self, fname, lname, email, mobile, password, cnf_password, address):
        url = reverse('regristration_req')
        data = {
            "fname": fname, "lname": lname, "email": email,
            "mobile": mobile, "password": password,
            "cnf_password": cnf_password, "address": address
        }
        response = self.client.post(url, data, format="json")
        return response

    def test_user_regristration(self):
        """Ensure we can create a ner user and retrieve it"""
        fname = "fname"
        lname = "lname"
        email = "email"
        mobile = "940171369"
        password = "password"
        cnf_password = "password"
        address = "address"

        response = self.post_user_regirstration(
            fname, lname, email, mobile, password, cnf_password, address)
        
        data = json.loads(response.content)
        print("Response: {0}\n".format(data))
        
        print("PK: {0}\n".format(UserRegistration.objects.get().pk))

        assert data['status_code'] == status.HTTP_200_OK

    def test_user_regristration_diferent_password(self):
        """Ensure we can create a ner user and retrieve it"""
        fname = "fname"
        lname = "lname"
        email = "email"
        mobile = "940171369"
        password = "pass"
        cnf_password = "pas"
        address = "address"

        response = self.post_user_regirstration(
            fname, lname, email, mobile, password, cnf_password, address)
        
        data = json.loads(response.content)
        print("Response: {0}\n".format(data))
        

        assert data['status_code'] == status.HTTP_400_BAD_REQUEST
    def test_user_regristration_one_field_null(self):
        """Ensure we can create a ner user and retrieve it"""
        fname = None
        lname = "lname"
        email = "email"
        mobile = "940171369"
        password = "password"
        cnf_password = "password"
        address = "address"

        response = self.post_user_regirstration(
            fname, lname, email, mobile, password, cnf_password, address)
        
        data = json.loads(response.content)
        print("Response: {0}\n".format(data))
        

        assert data['status_code'] == status.HTTP_400_BAD_REQUEST

    def test_user_regristration_for_mobile_number_error(self):
        """Ensure we can create a ner user and retrieve it"""
        fname = "fname"
        lname = "lname"
        email = "email"
        mobile = "9401713699"
        password = "password"
        cnf_password = "password"
        address = "address"

        response = self.post_user_regirstration(
            fname, lname, email, mobile, password, cnf_password, address)
        
        data = json.loads(response.content)
        print("Response: {0}\n".format(data))
        

        assert data['status_code'] == status.HTTP_400_BAD_REQUEST
