from django.urls import path
from user_model import views

urlpatterns = [
    path('', views.regristration_req, name='regristration_req'),
]
