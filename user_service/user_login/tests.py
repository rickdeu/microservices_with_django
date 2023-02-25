from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json


class UserLoginTests(APITestCase):
    def post_user_regirstration(self, fname, lname, email, mobile, password, cnf_password, address):
        url = reverse('regristration_req')
        data = {
            "fname": fname, "lname": lname, "email": email,
            "mobile": mobile, "password": password,
            "cnf_password": cnf_password, "address": address
        }
        response = self.client.post(url, data, format="json")
        return response

    def post_user_login(self, uname, password):
        url = reverse('user_login')
        data = {"uname": uname, "password": password}
        response = self.client.post(url, data, format="json")
        return response

    def test_user_login(self):
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
        assert data['status_code'] == status.HTTP_200_OK

        """Teste login function"""
        uname = "email"
        password = "password"

        response_login = self.post_user_login(uname, password)
        data1 = json.loads(response_login.content)

        print("Response: {0}\n".format(data1))
        assert data1['status_code'] == status.HTTP_200_OK

    def test_user_login_invalid_email(self):
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
        assert data['status_code'] == status.HTTP_200_OK

        """Teste login function"""
        uname = "myemail"
        password = "password"

        response_login = self.post_user_login(uname, password)
        data1 = json.loads(response_login.content)

        print("Response: {0}\n".format(data1))
        assert data1['status_code'] == status.HTTP_400_BAD_REQUEST

    def test_user_login_invalid_password(self):
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
        assert data['status_code'] == status.HTTP_200_OK

        """Teste login function"""
        uname = "email"
        password = "passworderror"

        response_login = self.post_user_login(uname, password)
        data1 = json.loads(response_login.content)

        print("Response: {0}\n".format(data1))
        assert data1['status_code'] == status.HTTP_400_BAD_REQUEST
