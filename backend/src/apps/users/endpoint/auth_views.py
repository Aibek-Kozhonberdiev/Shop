from rest_framework.views import APIView, Response
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from ..serializers import SerializerSetUser


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
        except TokenError:
            return Response({'detail': 'The token is invalid.'}, status=400)
