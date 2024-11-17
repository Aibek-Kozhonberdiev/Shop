from rest_framework.routers import DefaultRouter

from .views import ComplainView, SupportView, SupportListView

router = DefaultRouter()
router.register(r'complain', ComplainView, basename='complain')
router.register(r'supports', SupportView, basename='support')
router.register(r'list-supports', SupportListView, basename='support-admin')

urlpatterns = [

]

urlpatterns += router.urls
