from django.contrib import admin
from django.urls import path, include
from .views import IndexView, BaseLogoutView, NewsView

from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('tinymce/', include('tinymce.urls')),

    path('admin/', admin.site.urls),
    path('accounts/logout/', BaseLogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('posts/', include('app.urls')),
    path('news/', NewsView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
