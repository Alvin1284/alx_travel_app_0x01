from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r"listings", ListingViewSet)
router.register(r"bookings", BookingViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Travel API",
        default_version="v1",
        description="API for listing and booking travel accommodations",
    ),
    public=True,
)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
