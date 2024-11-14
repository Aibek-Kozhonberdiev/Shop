from rest_framework.routers import DefaultRouter

from .views import ShopSetView

router = DefaultRouter()
router.register(r'shops', ShopSetView, basename='shop')

urlpatterns = [

]

urlpatterns += router.urls
