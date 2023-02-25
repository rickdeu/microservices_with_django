from __future__ import unicode_literals
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import ProductDetails

@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}

    # This will fetch the data from the database
    proddata = ProductDetails.objects.all()
    for tbl_value in proddata.values():
        data.append(tbl_value)
    # If data is avalibe then it returns the data
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = 200
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = 400
        resp['data'] = "Data is not available."
    
    return HttpResponse(json.dumps(resp), content_type='application/json')