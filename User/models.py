from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add any additional fields specific to the Supervisor model here
    # For example:
    # age = models.PositiveIntegerField(null=True, blank=True)
    
    # By default, Supervisor model will have all the fields of AbstractUser:
    # - username
    # - first_name
    # - last_name
    # - email
    # - password
    # - ...

    def __str__(self):
        return self.username
