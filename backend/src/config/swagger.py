from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Online shop API",
      default_version='#',
      description="#",
      terms_of_service="#",
      contact=openapi.Contact(email="ratroniii@gmail.com"),
      license=openapi.License(name="#"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,)
)
