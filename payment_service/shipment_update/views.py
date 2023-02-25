
from __future__ import unicode_literals
from payment.models import PaymentStatus as paystat
import requests
import json

### This function is for fetching the user data
def shipment_details_update(uname):
    ship_dict = {}
    ### It is used for getting data from payment info
    user = paystat.objects.filter(username = uname)
    data = [value for value in user.values()]
    ship_dict['product_id'] == data['pruduct_id']
    ship_dict['quantity'] == data['quantity']
    ship_dict['payment_status'] == data['status']
    ship_dict['transaction_id'] == data['id']
    ship_dict['mobile'] == data['mobile']

    ### It is used for getting the user info
    url = 'http://127.0.0.1:8000/userinfo/'
    d1 = {}
    d1['username'] = data['username']
    data = json.dumps(d1)

    headers = {'Content-Type':"application/json"}
    response = requests.post(url, data=data, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    ship_dict['fname'] = val1['data']['fname']
    ship_dict['lname'] = val1['data']['lname']
    ship_dict['address'] = val1['data']['address']
    ship_dict['email'] = val1['data']['email']

    ### Data is ready for calling the shipment_updates API
    url = 'http://127.0.0.1:5000/shipment_updates/'
    data = json.dumps(ship_dict)
    headers = {'Content-Type':"application/json"}
    response = requests.post(url, data=data, headers=headers)
    api_resp = json.loads(response.content.decode("utf-8"))
    return api_resp