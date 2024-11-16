from rest_framework.routers import DefaultRouter

from .views import ComplainView, SupportView

router = DefaultRouter()
router.register(r'complain', ComplainView, basename='complain')
router.register(r'supports', SupportView, basename='support')

urlpatterns = [

]

urlpatterns += router.urls
