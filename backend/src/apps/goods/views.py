from django.contrib.auth import get_user_model
from rest_framework.views import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView

from .models import Product, ProductFoto, Category, SubCategory, ProposalNewCategory
from .serializers import SerializerProduct, SerializerProductFoto, SerializerCategory, SerializerSubCategory

User = get_user_model()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct


class ProductFotoViewSet(viewsets.ModelViewSet):
    queryset = ProductFoto.objects.all()
    serializer_class = SerializerProductFoto
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return ProductFoto.objects.none()

        if not hasattr(self.request.user, 'shop'):
            raise SerializerProduct.ValidationError("The user does not have an associated store.")

        return ProductFoto.objects.filter(product__shop=self.request.user.shop)


class CategoryView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        context = {
            "category": SerializerCategory(Category.objects.all(), many=True).data,
            "set_category": SerializerSubCategory(SubCategory.objects.all(), many=True).data
        }
        return Response(context, status=200)

    def post(self, request):
        try:
            user = User.objects.get(username=self.request.user.username)
            if not request.data.get('text'):
                raise User.DoesNotExist
            ProposalNewCategory.objects.create(
                text=request.data.get('text'),
                user=user
            )
            return Response({"detail": "не работает (это временно) :("}, status=200)
        except User.DoesNotExist:
            return Response({"detail": "Incorrect user data (token) or missing text."}, status=400)
