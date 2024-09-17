from rest_framework.routers import DefaultRouter

from .views import UserVieSet

router = DefaultRouter()
router.register(r'users', UserVieSet, basename='user')

urlpatterns = [

]

urlpatterns += router.urls
