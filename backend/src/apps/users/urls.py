from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import UserView, UserRegister, UserAuthOrLogout, UserConfirmation

router = DefaultRouter()
router.register(r'users', UserView, basename='user')

urlpatterns = [
    path('registration', UserRegister.as_view(), name="registration_api"),
    path('auth_or_logout', UserAuthOrLogout.as_view(), name="user_api"),
    path('user_chek', UserConfirmation.as_view(), name='chak'),
]

urlpatterns += router.urls
