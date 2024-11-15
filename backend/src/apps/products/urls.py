from rest_framework.routers import DefaultRouter

from .views import ProductSetView, FotoProductSetView, SubCategorySetView

router = DefaultRouter()
router.register(r'products', ProductSetView, basename='products')
router.register(r'products/photos', FotoProductSetView, basename='foto_product')
router.register(r'categories', SubCategorySetView, basename='category')

urlpatterns = [

]

urlpatterns += router.urls
