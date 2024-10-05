from django.urls import path, include


urlpatterns = [
    # CustomUser
    path('', include("apps.users.urls")),

    # Shops and ratings
    path('', include("apps.shops.urls")),
]
