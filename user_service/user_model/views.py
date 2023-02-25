from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import UserRegistration

### This function is inserting the data into our table
def data_insert(fname, lname, email, mobile, password, address):
    user_data = UserRegistration(fname=fname, lname=lname, email=email, mobile=mobile, password=password, address=address)
    user_data.save()
    return 1

### This function will get tge data from the front end
@csrf_exempt
def regristration_req(request):
        ### The following are the input fields
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            fname = val1.get("fname")
            lname = val1.get("lname")
            email = val1.get("email")
            mobile = val1.get("mobile")
            password = val1.get("password")
            cnf_password = val1.get("cnf_password")
            address = val1.get("address")
            resp = {}
            #### In this if statement, checking that all fields area available
            if fname and lname and email and mobile and password and cnf_password and address:
                ### This wiil check that the mobile number is only 10 digits
                if len(str(mobile)) == 9:
                    ### It will check that password and confirm password both ate the same
                    if password == cnf_password:
                        ### After all validation, it will call the data_insert function
                        respdata = data_insert(fname, lname, email, mobile, password, address)
                        ### If it returns value then wiil show success
                        if respdata:
                            resp['status'] = 'Success'
                            resp['status_code'] = 200
                            resp['message'] = 'User is registered Successfully'
                        ### If it is not returning any value then the show will fail
                        else:
                            resp['status'] = 'Failed'
                            resp['status_code'] = 400
                            resp['message'] = 'Unable to register user, Please try again'
                    ### It the password and confirm password is not matched then it will be through error
                    else:
                            resp['status'] = 'Failed'
                            resp['status_code'] = 400
                            resp['message'] = 'Password and Confirm password should be same'
                ### If the mobile number is not in 10 digits then it will be through error
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = 400
                    resp['message'] = 'Mobile number should be 9 digit'
            ### If any mandatory field is missing then it will be through a failed message
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = 400
                resp['message'] = 'All fields are mandatory'
    return HttpResponse(json.dumps(resp), content_type='application/json')