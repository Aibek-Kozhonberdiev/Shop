from django.urls import path, include

urlpatterns = [
    path('', include('apps.users.urls')),
    path('', include('apps.shops.urls')),
    path('', include('apps.ratings.urls')),
    path('', include('apps.products.urls')),
    path('', include('apps.complaints.urls')),
    path('', include('apps.chats.urls')),
]
