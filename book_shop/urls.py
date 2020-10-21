from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from library import views

urlpatterns = [
    path('', views.main_page, name="base"),
    path('library/', include('library.urls')),
    path('admin/', admin.site.urls, name="admin")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)