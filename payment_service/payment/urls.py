from django.urls import path
from payment import views

urlpatterns = [
    path('', views.get_payment, name='initiate_payment'),
    path('payment_status/', views.get_transaction_details, name='payment_status'),

]
