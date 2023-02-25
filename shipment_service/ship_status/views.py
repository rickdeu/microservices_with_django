from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ship_status.models import Shipment as ship_obj
import json

### This function is inserting the data into our table
def ship_data_insert(fname, lname, email, mobile, address, product_id, quantity, payment_status, transaction_id, shipment_status):
    shipment_data = ship_obj(fname=fname, lname=lname, email=email, mobile=mobile, address=address, product_id=product_id, quantity=quantity, payment_status=payment_status, transaction_id=transaction_id, shipment_status=shipment_status)
    shipment_data.save()
    return 1

@csrf_exempt
def shipment_reg_update(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            ### This is for reading the inputs from JSON.
            fname = val1.get("fname")
            lname = val1.get("lname")
            email = val1.get("email")
            mobile = val1.get("mobile")
            address = val1.get("address")
            product_id = val1.get("product_id")
            quantity = val1.get("quantity")
            payment_status = val1.get("payment_status")
            transaction_id = val1.get("transaction_id")
            shipment_status = "ready to dispatch"

            resp = {}
            ### After all validation, it will cal the data_insert function
            respdata = ship_data_insert(fname, lname, email, mobile, address, product_id, quantity, payment_status, transaction_id, shipment_status)

            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = 200
                resp['message'] = "Product is ready to dispatch."
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = 400
                resp['message'] = "Failed to update shipment details."
    return HttpResponse(json.dumps(resp), content_type='application/json')

### This function is used for finding the transaction
def shipment_data(uname):
    data = ship_obj.objects.filter(email=uname)
    for val in data.values():
        return val

### This function is used for getting the shipment status
@csrf_exempt
def shipment_status(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            variable1 = json.loads(request.body)
            ### This is for reading the inputs from JSON
            uname = variable1.get('email')
            resp = {}
            ### It will call the shipment_data function
            respdata = shipment_data(uname)
            ### If it returns value then will show success
            if respdata:
                resp['status']= 'Sucess'
                resp['status_code'] = 200
                resp['message'] = respdata
            ### If it is not returning any value then it will show failed response
            else:
                resp['status']= 'Failed'
                resp['status_code'] = 400
                resp['message'] = "User data is not availabe."
    return HttpResponse(json.dumps(resp), content_type='application/json')