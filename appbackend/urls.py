
from django.contrib import admin
from django.urls import path, include
from . import views
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("count/", include("countapi.urls")),
    path("auth/", include("authapi.urls")),
    path("health/", views.HealthCheck.as_view()),
    path("test/", include("testapi.urls")),
    path("posts/", include("postapi.urls")),
    path("wisdom/", include("wisdom.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
