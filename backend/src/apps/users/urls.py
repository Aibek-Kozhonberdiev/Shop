from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()
router.register(r'users', views.UserSetView.as_view(), basename='user')

urlpatterns = [
    path('registration', views.UserRegister.as_view()),

    path('auth', views.UserAuthOrLogout.as_view({'post': 'post'})),
    path('logout', views.UserAuthOrLogout.as_view({'delete': 'delete'})),

    path('check_email', views.EmailConfirmation.as_view({'get': 'get'})),
    path('key_email', views.EmailConfirmation.as_view({'post': 'post'})),
]

urlpatterns += router.urls
