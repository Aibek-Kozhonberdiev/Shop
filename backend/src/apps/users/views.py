import random
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.views import Response, APIView
from rest_framework import mixins, viewsets, permissions
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SerializerSetUser
from .tasks import send_key, time_valid_key

User = get_user_model()


class UserSetView(mixins.ListModelMixin,
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

    def delete(self, request):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response({'detail': 'Successfully logged out.'}, status=205)
        except TokenError as e:
            return Response({'detail': 'The token is invalid.'}, status=400)


class EmailConfirmation(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def generate_key(self):
        key = ''
        for _ in range(1, 10):
            key += random.randint(0, 9)
        return key

    def key_save(self, user):
        key = self.generate_key()
        user.key = make_password(key)
        user.key_valid = True
        user.save()
        return key

    def send_email_key(self, user):
        key = self.key_save(user)
        send_key.delay(user.email, key)
        time_valid_key.delay(user)

    def get(self):
        user = self.request.user
        if not user.email_confirmed:
            self.send_email_key(user)
            return Response({'detail': "The key has been sent to your email."}, status=201)
        else:
            return Response({'detail': "User verified."}, status=200)

    def post(self, request):
        user = self.request.user
        key = request.data.get('key')
        if not user.key_valid:
            return Response({'detail': 'Time expired to confirm key.'}, status=401)
        if user.key == make_password(key):
            user.email_confirmed = True
            user.key_valid = False
            user.save()
            return Response({'detail': 'Email was successfully verified.'}, status=201)
        return Response({'detail': 'Invalid key.'}, status=500)


class PhoneConfirmation(EmailConfirmation):
    def send_phone_key(self):
        pass

    def get(self):
        pass

    def post(self):
        pass
