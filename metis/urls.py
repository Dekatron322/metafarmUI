from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("stake/", include("stake.urls")),
    path("wallet/", include("wallet.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)