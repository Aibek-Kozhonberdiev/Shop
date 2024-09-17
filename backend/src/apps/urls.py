from django.urls import path, include


urlpatterns = [
    # CustomUser
    path('', include("apps.users.urls"))
]
