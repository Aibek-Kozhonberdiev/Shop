from rest_framework.views import Response
from rest_framework import permissions, viewsets

from ..tasks import send_key_email, send_phone
from ..services.key_generate import KeyGenerate


class EmailConfirmation(viewsets.GenericViewSet, KeyGenerate):
    permission_classes = [permissions.IsAuthenticated, ]
    send_type = 'email'

    def send_key(self, user):
        key = self.key_save(user)
        send_key_email.delay(user.email, key)

    def get(self):
        user = self.request.user
        if not user.email_confirmed:
            self.send_key(user)
            return Response({'detail': f"The key has been sent to your {self.send_type}."}, status=201)
        else:
            return Response({'detail': "User verified."}, status=200)

    def post(self, request):
        user = self.request.user
        key = request.data.get('key')
        if not self.key_data_check(user):
            return Response({'detail': 'Time expired to confirm key.'}, status=401)
        if self.key_check(user, key):
            user.email_confirmed = True
            user.save()
            return Response({'detail': 'Key was successfully verified.'}, status=201)
        return Response({'detail': 'Invalid key.'}, status=401)


class PhoneConfirmation(EmailConfirmation):
    send_type = 'phone'

    def send_key(self, user):
        key = self.key_save(user)
        send_phone.delay(user.phone, key, 5)
