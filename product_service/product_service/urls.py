from django.contrib import admin
from django.urls import path, include
from product_model import urls as product_model_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_product_data', include(product_model_urls)),
]
