"""deeptech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django_otp.admin import OTPAdminSite
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# admin.site.__class__ = OTPAdminSite

admin.site.site_header = "DeepTech API"
admin.site.site_title = "DeepTech API Admin Portal"
admin.site.index_title = "Welcome to DeepTech API"

schema_view = get_schema_view(
    openapi.Info(
        title="DeepTech API",
        default_version="v1",
        description="Backend API for data",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="data@astral-aerial.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(r"redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    url(r"^raster/", include("raster.urls")),
    path("api/farmers/", include("accounts.api.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
