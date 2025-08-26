from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Документация",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("", include("tracker.urls", namespace="tracker")),
    # Документация
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="docs"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
