from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from google.oauth2 import id_token
from google.auth.transport import requests


User = get_user_model()

def check_google_token(google_user):
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request())
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google.')

    user, is_created = User.objects.get_or_create(
        email=google_user['email'],
    )
    if is_created:
        user.username = google_user['username']
        user.save()
    return user
