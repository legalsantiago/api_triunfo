from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api_triunfo.users.views import login,logout
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)


schema_view = get_schema_view(
   openapi.Info(
      title="Swagger Api",
      default_version='V1',
      description="Test Swagger documentation",
      terms_of_service="http://127.0.0.1:8000/",
      contact=openapi.Contact(email="santiagotriunfobet1@gmail.com"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login.as_view(), name='login'),
    #path('logout', logout.as_view(), name='logout'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('',include('api_triunfo.users.api.routers')),
    path('api/token/', TokenObtainPairView.as_view(), name='obtener new token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist')
    
]
