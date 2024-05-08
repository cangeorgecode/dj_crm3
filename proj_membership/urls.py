from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('membership/', include('membership.urls')),
    path('membership/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
]
