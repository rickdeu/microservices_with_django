from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import UserRegistration


# This function is created for validating the user
def user_validation(uname, password):
    user_data = UserRegistration.objects.filter(email=uname, password=password)
    if user_data:
        return "Valid User"
    else:
        return "Invalid User"


# This function is created for getting the user name and password
@csrf_exempt
def user_login(request):
        ### The following are the input fields
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('uname')
            password = val1.get('password')

            resp = {}

            print(f"Name: {uname}")

            if uname and password:
                # Calling the user_validation function for username and password validation
                respdata = user_validation(uname, password)

                # If a user is valid then it gives success as a response
                if respdata == 'Valid User':
                    resp['status'] = 'Success'
                    resp['status_code'] = 200
                    resp['message'] = 'Welcome to Ecommerce website......'
                elif respdata == 'Invalid User':
                    resp['status'] = 'Failed'
                    resp['status_code'] = 400
                    resp['message'] = 'Invalid credentials.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = 400
                resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
