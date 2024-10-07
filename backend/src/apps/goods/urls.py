from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductFotoViewSet, CategoryView


router = DefaultRouter()
router.register(r"product", ProductViewSet, basename="product")
router.register(r"product_foto", ProductFotoViewSet, basename="product_foto")

urlpatterns = [
    path("category", CategoryView.as_view(), name="category"),
]

urlpatterns += router.urls
