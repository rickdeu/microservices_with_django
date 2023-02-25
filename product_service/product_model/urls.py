from django.urls import path
from product_model import views

urlpatterns = [
    path('', views.get_product_data, name='get_product_data'),
]