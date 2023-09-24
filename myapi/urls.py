from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

handler404 = 'api.views.custom_404'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("api/", include("api.urls")),
]
