from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title=settings.NAME_SHOP,
      default_version='#',
      description="#",
      terms_of_service="#",
      contact=openapi.Contact(email=settings.EMAIL_HOST_USER),
      license=openapi.License(name="#"),
   ),
   public=True,
   permission_classes=(permissions.IsAdminUser,)
)
