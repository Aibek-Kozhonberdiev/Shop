from rest_framework.routers import DefaultRouter

from .views import ShopViewSet, ComplaintView, RatingView

router = DefaultRouter()
router.register(r"shop", ShopViewSet, basename='shop')
router.register(r"complaint", ComplaintView, basename='complaint')
router.register(r"rating", RatingView, basename='rating')

urlpatterns = [

]

urlpatterns += router.urls
