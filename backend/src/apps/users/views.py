import random
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.views import Response, APIView
from rest_framework import mixins, viewsets, permissions
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SerializerSetUser
from .tasks import send_key

User = get_user_model()


class UserView(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    serializer_class = SerializerSetUser
    queryset = User.objects.all()


class UserRegister(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = SerializerSetUser(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        user_data = {
            'user': SerializerSetUser(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(user_data, status=201)


class UserAuthOrLogout(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = SerializerSetUser(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        user_data = {
            'user': SerializerSetUser(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(user_data, status=201)

    def delite(self, request):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response({'detail': 'Successfully logged out.'}, status=205)
        except TokenError as e:
            return Response({'detail': 'The token is invalid.'}, status=400)


class UserConfirmation(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def generate_key(self):
        key = ''
        for _ in range(1, 10):
            key += random.randint(0, 9)
        return key

    def send_email_key(self, user):
        key = self.generate_key()
        user.key = make_password(key)
        user.save()
        email = user.email
        send_key.delay(email, key)

    def get(self, request):
        user = self.request.user
        if request.query_params['email'] == "email":
            self.send_email_key(user)
            return Response({'detail': "The key has been sent to your email."}, status=201)
        else:
            return Response({'detail': "Sending a confirmation code to the number is not possible yet."}, status=300)

    def post(self, request):
        user = self.request.user
        key = request.data.get('key')
        if user.key == make_password(key):
            if request.query_params['send'] == "email":
                user.email_confirmed = True
            elif request.query_params['send'] == "phone":
                user.phone_confirmed = True
            user.save()
            return Response({'detail': f'{request.query_params["email"].title()} was successfully verified.'}, status=201)
        return Response({'detail': 'Invalid key.'}, status=500)
