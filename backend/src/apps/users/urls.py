from rest_framework.routers import DefaultRouter
from django.urls import path

from .endpoint import views, auth_views, key_views

router = DefaultRouter()
router.register(r'users', views.UserSetView, basename='user')

urlpatterns = [
    path('registration', auth_views.UserRegister.as_view({'post': 'post'})),

    path('auth', auth_views.UserAuthOrLogout.as_view({'post': 'post'})),
    path('logout', auth_views.UserAuthOrLogout.as_view({'delete': 'delete'})),

    path('check_email', key_views.EmailConfirmation.as_view({'get': 'get'})),
    path('key_email', key_views.EmailConfirmation.as_view({'post': 'post'})),

    path('check_phone', key_views.PhoneConfirmation.as_view({'get': 'get'})),
    path('key_phone', key_views.PhoneConfirmation.as_view({'post': 'post'})),
]

urlpatterns += router.urls
