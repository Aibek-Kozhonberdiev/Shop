from rest_framework.routers import DefaultRouter

from .views import ComplainView, SupportMessageView

router = DefaultRouter()
router.register(r'complain', ComplainView, basename='complain')
router.register(r'supports', SupportMessageView, basename='support')

urlpatterns = [

]

urlpatterns += router.urls
