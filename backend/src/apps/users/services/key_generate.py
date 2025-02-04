import random
import datetime
from django.contrib.auth.hashers import make_password


class KeyGenerate:
    def __init__(self, size=10):
        self.size = size

    def key_generate(self):
        key = ''
        for _ in range(1, self.size):
            key += random.randint(0, 9)
        return key


class KeySave:
    @staticmethod
    def key_save(user, key):
        user.key = make_password(key)
        user.key_data = datetime.datetime.now()
        user.key_valid = True
        user.save()

    @staticmethod
    def key_data_check(user):
        if (datetime.datetime.now() - user.key_data) < datetime.timedelta(minutes=5):
            return True
        return False

    @staticmethod
    def key_check(user, key):
        if key == make_password(user.key):
            return True
        return False
