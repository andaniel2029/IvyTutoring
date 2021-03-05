from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	date_birth  = models.DateField(null=True)
	user_type = models.IntegerField(null=True)
	email_confirm = models.BooleanField(default=False)

