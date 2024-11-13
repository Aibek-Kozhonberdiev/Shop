import random
import datetime
from django.contrib.auth.hashers import make_password


class KeyGenerate:
    def key_generate(self):
        key = ''
        for _ in range(1, 10):
            key += random.randint(0, 9)
        return key

    def key_save(self, user):
        key = self.key_generate()
        user.key = make_password(key)
        user.key_data = datetime.datetime.now()
        user.key_valid = True
        user.save()
        return key

    def key_data_check(self, user):
        if (datetime.datetime.now() - user.key_data) < datetime.timedelta(minutes=5):
            return True
        return False

    def key_check(self, user, key):
        if key == make_password(user.key):
            return True
        return False
