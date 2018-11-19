from django.db import models

# Create your models here.
from accounts.models import User


class Like(models.Model):
    member = models.ForeignKey(User, related_name="member", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
