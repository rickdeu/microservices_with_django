from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import UserRegistration as userreg


# This function is for fetching the user data
def user_data(uname):
    user = userreg.objects.filter(email=uname)
    for data in user.values():
        return data

# This function is created for getting the username and password.


@csrf_exempt
def user_info(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('uname')
            if uname:
                # Calling the getting the user info
                respdata = user_data(uname)
                dict1 = {}
                if respdata:
                    dict1['fname'] = respdata.get('fname', '')
                    dict1['lname'] = respdata.get('lname', '')
                    dict1['mobile'] = respdata.get('mobile', '')
                    dict1['email'] = respdata.get('email', '')
                    dict1['address'] = respdata.get('address', '')
                if dict1:
                    resp['status'] = 'Success'
                    resp['status_code'] = 200
                    resp['data'] = dict1
                # If a user is not found then it give failed as a response
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = 400
                    resp['message'] = "User Not Found."
            # The field value is missing
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = 400
                resp['message'] = "Fields is mandatory"
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = 400
            resp['message'] = "Request type is not matched"
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = 400
        resp['message'] = "Request type is not matched"
    return HttpResponse(json.dumps(resp), content_type='application/json')
