from django.contrib import admin
from django.urls import path, include
from core.routers import urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(urlpatterns)),
]
