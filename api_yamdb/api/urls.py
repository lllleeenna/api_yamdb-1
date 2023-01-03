from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ( UserViewSet, generator_token, generator_code)

router = DefaultRouter()

router.register(r"users", UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', generator_code, name='generator_code'),
    path('v1/auth/token/', generator_token, name='generator_token')
]
