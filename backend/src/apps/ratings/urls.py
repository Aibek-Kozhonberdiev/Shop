from rest_framework.routers import DefaultRouter

from .views import RatingShopView, RatingProductView

router = DefaultRouter()
router.register(r'ratings-shop', RatingShopView, basename='shop_rating')
router.register(r'ratings-product', RatingProductView, basename='product_rating')

urlpatterns = [

]

urlpatterns += router.urls
