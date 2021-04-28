from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('blog.urls', namespace='blog')),
    path("feedback/", include('feedback.urls', namespace='feedback')),
    path("", include('account.urls', namespace='account')),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)