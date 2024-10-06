from django.urls import path
from rest_framework.authtoken import views

from .views import user_register

urlpatterns = [
    path('register/', user_register),
    path('token-auth/', views.obtain_auth_token),
]
