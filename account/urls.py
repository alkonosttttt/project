from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", Registration.as_view(), name="Registration"),
]