from rest_framework.authtoken import views
from rest_framework_simplejwt.views  import TokenObtainPairView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(r'token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', views.obtain_auth_token),
]
