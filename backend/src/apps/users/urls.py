from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import UserVieSet, registration, auth, logout_user

router = DefaultRouter()
router.register(r'users', UserVieSet, basename='user')

urlpatterns = [
    path('registration', registration, name="registration_api"),
    path('auth', auth, name="user_api"),
    path('logout_user', logout_user, name="logout_api"),
]

urlpatterns += router.urls
