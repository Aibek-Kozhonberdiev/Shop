import random
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password, make_password
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
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'Incorrect email address or password.'}, status=401)
        if not check_password(password, user.password):
            return Response({'detail': 'Incorrect email address or password.'}, status=401)
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
        return random.randint(10000, 99999)

    def send_email_key(self, user):
        key = self.generate_key()
        user.key = make_password(key)
        user.save()
        email = user.email
        send_key.delay(email, key)

    def get(self, request, send):
        user = self.request.user
        if send == "email":
            self.send_email_key(user)
            return Response({'detail': "The key has been sent to your email."}, status=201)
        else:
            return Response({'detail': "Sending a confirmation code to the number is not possible yet."}, status=300)

    def post(self, request, send):
        user = self.request.user
        key = request.data.get('key')
        if user.key == make_password(key):
            if send == "email":
                user.email = True
            user.save()
            return Response({'detail': f'{send.title()} was successfully verified.'}, status=201)
        return Response({'detail': 'Invalid key.'}, status=500)
