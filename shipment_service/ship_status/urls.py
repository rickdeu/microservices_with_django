from django.urls import path
from ship_status import views


urlpatterns = [
    path('', views.shipment_reg_update, name='shipment_reg_update'),
    path('shipment_status', views.shipment_status, name='shipment_status'),
]
