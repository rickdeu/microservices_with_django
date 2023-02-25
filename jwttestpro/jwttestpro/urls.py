from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from jwttestpro.views import HelloView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/testjwt/', HelloView.as_view(), name='tokentest'),
    path('api/token/refress/', TokenRefreshView.as_view(), name='token_refresh'),
]
