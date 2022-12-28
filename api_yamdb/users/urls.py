from rest_framework.authtoken import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('signup/', views.obtain_auth_token),
]
