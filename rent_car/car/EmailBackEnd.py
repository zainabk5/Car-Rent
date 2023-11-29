
from django.contrib.auth.backends import ModelBackend
from car.models import *

class EmailBack(ModelBackend):
    def authenticate(self, request, useremail=None, userpassword=None, **kwargs):
        try:
            user = User.objects.get(useremail=useremail)
        except User.DoesNotExist:
            return None
        else:
            if user.userpassword == userpassword:
                return user
        return None
