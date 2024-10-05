from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions

from .models import Shop, Complaint, Rating
from .serializers import SerializerShop, SerializerComplaint, SerializerRating

User = get_user_model()


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = SerializerShop


class ComplaintView(viewsets.ModelViewSet):
    """
    Отображает жалобы только от пользователя, отправившего запрос.
    """
    queryset = Complaint.objects.all()
    serializer_class = SerializerComplaint
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Complaint.objects.filter(user=self.request.user)


class RatingView(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = SerializerRating
