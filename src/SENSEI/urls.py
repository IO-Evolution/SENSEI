from django.contrib import admin
from django.urls import path, include

# APPS
from FSE import urls as FSE_URLS

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('FSE/', include(FSE_URLS))
]
