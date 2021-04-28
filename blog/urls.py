from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('', BaseView.as_view(template_name='base.html')),
    path('links/', BaseView.as_view(template_name='links.html')),
    path('blog/', PostList.as_view()),
    path('blog/<slug:slug>/', PostDetail.as_view()),
]

