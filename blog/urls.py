from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('', BaseView.as_view(template_name='base.html')),
    path('video/', BaseView.as_view(template_name='video.html')),
    path('post/', ArticleAddView.as_view()),
    path('links/', BaseView.as_view(template_name='links.html')),
    path('blog/', PostList.as_view()),
    path('blog/<slug:slug>/', PostDetail.as_view()),
]

