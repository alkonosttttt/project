from django.urls import path
from .views import *

app_name = "feedback"

urlpatterns = [
    path("", FeedbackView.as_view(), name="feedback"),
]