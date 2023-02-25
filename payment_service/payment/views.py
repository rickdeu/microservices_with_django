from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from payment.models import PaymentStatus as paystat
from shipment_update.views import shipment_details_update as ship_update

# This function is for fetching the user data


def get_transaction_details(uname):
    user = paystat.objects.filter(username=uname)
    for data in user.values():
        return data

# This function is used for storing the data


def store_data(uname, prodid, price, quantity, mode_of_payment, mobile):
    user_data = paystat(username=uname, product_id=prodid, price=price, quantity=quantity,
                        mode_of_payment=mode_of_payment, mobile=mobile, status='Success')
    user_data.save()
    return 1

# THis function is created for getting the payment


@csrf_exempt
def get_payment(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('uname')
            prodid = val1.get("product_id")
            price = val1.get("price")
            quantity = val1.get("quantity")
            mode_of_payment = val1.get("mode_of_payment")
            mobile = val1.get("mobile")

            if uname and prodid and price and quantity and mode_of_payment and mobile:
                # It will cal the store data function
                respdata = store_data(uname, prodid, price, quantity, mode_of_payment, mobile)
                respdata2 = ship_update(uname)

                # If it returns value then will show success
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = 200
                    resp['message'] = 'Transaction is completed'
                # If it is return null value then will show failed message
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = 400
                    resp['message'] = 'Transaction is failed, Please try again'
            # If any mandatory field is missing then it will be through a failed message
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = 400
                resp['message'] = 'All fields are mandatory'
    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def user_transaction_info(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('uname')
            if uname:
                # Calling the getting the user info
                respdata = get_transaction_details(uname)
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = 200
                    resp['message'] = respdata
                # If a user is not found then it give failed as response
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = 400
                    resp['message'] = 'User Not Found'
            # If the value is missing
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = 400
                resp['message'] = 'Fields is mandatory'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = 400
            resp['message'] = 'Request type is not matched'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = 400
        resp['message'] = 'Request type is not matched'
    return HttpResponse(json.dumps(resp), content_type='application/json')
