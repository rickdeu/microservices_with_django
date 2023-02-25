from django.contrib import admin
from django.urls import path, include

# import urls for apps
from user_model import urls as user_model_urls
from user_info import urls as user_info_urls
from user_login import urls as user_login_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userregistration/', include(user_model_urls)),
    path('userinfo/', include(user_info_urls)),
    path('userlogin/', include(user_login_urls)),
]
