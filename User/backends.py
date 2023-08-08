from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q  

class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None,email=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(UserModel)
        try:
            user = UserModel.objects.get(Q(username=username) | Q(email=email))
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None
