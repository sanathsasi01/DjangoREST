from django.urls import path
from .views import *

from rest_framework.authtoken import views

urlpatterns = [
    path('', registration_api, name='registration'),
    path('login', views.obtain_auth_token, name='login')
]