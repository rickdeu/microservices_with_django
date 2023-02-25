from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class UserInfoTests(APITestCase):
    def post_user_regirstration(self, fname, lname, email, mobile, password, cnf_password, address):
        url = reverse('regristration_req')
        data = {
            "fname": fname, "lname": lname, "email": email,
            "mobile": mobile, "password": password,
            "cnf_password": cnf_password, "address": address
        }
        response = self.client.post(url, data, format="json")
        return response
    def post_user_info(self, uname):
        url = reverse('user_info')
        data = {"uname": uname}
        response = self.client.post(url, data, format="json")
        return response

    def test_user_get_info(self):
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


        uname = "email"

        """Test user info"""
        response_info = self.post_user_info(uname)
        data1 = json.loads(response_info.content)

        print("Response: {0}\n".format(data1))
        assert data1['status_code'] == status.HTTP_200_OK
        assert data1['data']['email'] == email


    def test_user_get_info_email_error(self):
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


        uname = "myemail"

        """Test user info"""
        response_info = self.post_user_info(uname)
        data1 = json.loads(response_info.content)

        print("Response: {0}\n".format(data1))
        assert data1['status_code'] == status.HTTP_400_BAD_REQUEST

    def test_user_get_info_email_null(self):
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


        uname = None

        """Test user info"""
        response_info = self.post_user_info(uname)
        data1 = json.loads(response_info.content)

        print("Response: {0}\n".format(data1))
        assert data1['status_code'] == status.HTTP_400_BAD_REQUEST


