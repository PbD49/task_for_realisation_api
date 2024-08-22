from django.contrib import admin
from django.urls import path
from blogru.views import BlogAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API documentation powered by Swagger",
        terms_of_service="https://your-terms-of-service-url.com/",
        contact=openapi.Contact(email="contact@your-api.com"),
        license=openapi.License(name="Your API License"),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blogrulist/', BlogAPIView.as_view()),
    path('api/v1/blogrulist/<int:pk>/', BlogAPIView.as_view()),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
]
