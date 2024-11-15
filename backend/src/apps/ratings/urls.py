from rest_framework.routers import DefaultRouter

from .views import RatingShopView, RatingProductView, FotoRatingView

router = DefaultRouter()
router.register(r'ratings-shop', RatingShopView, basename='shop_rating')
router.register(r'ratings-product', RatingProductView, basename='product_rating')
router.register(r'rating-foto', FotoRatingView, basename='rating-foto')

urlpatterns = [

]

urlpatterns += router.urls
