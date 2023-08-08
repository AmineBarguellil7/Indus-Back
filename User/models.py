from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Additional fields
    isAdmin = models.BooleanField(default=False)
    isSupervisor = models.BooleanField(default=True)

    # By default, CustomUser model will have all the fields of AbstractUser:
    # - username
    # - first_name
    # - last_name
    # - email
    # - password
    # - ...

    def __str__(self):
        return self.username

