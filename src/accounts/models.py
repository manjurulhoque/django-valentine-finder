# from datetime import datetime, timezone
import django
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=256, blank=False)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=10, blank=False)
    age = models.IntegerField(blank=False)
    dob = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    looking_for = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    profile_picture = models.ImageField(null=True,
                                        blank=True,
                                        upload_to='photos',
                                        default='images/user.png',
                                        verbose_name="profile picture"
                                        )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'gender', 'age']

    def __unicode__(self):
        return self.username

    def is_liked_by_me(self, member_id, user_id):
        pass
