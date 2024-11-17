from rest_framework.views import Response
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from ..serializers import UserSerializer, GoogleSerializer
from ..services.google import check_google_token


class UserRegister(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        user_data = {
            'user': self.serializer_class(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(user_data, status=201)


class UserAuthOrLogout(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        user_data = {
            'user': self.serializer_class(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(user_data, status=200)

    def delete(self, request):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response({'detail': 'Successfully logged out.'}, status=205)
        except TokenError:
            return Response({'detail': 'The token is invalid.'}, status=401)


class UserAuthGoogle(viewsets.GenericViewSet):
    serializer_class = GoogleSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            user = check_google_token(data)
            refresh = RefreshToken.for_user(user)
            user_data = {
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(user_data, status=200)
        else:
            return AuthenticationFailed(detail='Bad data Google')
