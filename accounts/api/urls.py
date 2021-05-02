from django.urls import path
from .views import *

urlpatterns = [
    path('', registration_api, name='registration')
]