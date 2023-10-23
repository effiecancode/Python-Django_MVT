from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

from django.db import models

# Create your models here.

class ConsumerUser(AbstractUser):
    last_login = models.DateTimeField(
        verbose_name="Last Login", blank=True, null=True)
    username = models.CharField(max_length=120, null=True)
    date_joined = models.DateTimeField(
        verbose_name="Date Joined", auto_now_add=True)
    email = models.EmailField(
        verbose_name="Email address", max_length=100, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name + " " + self.last_name

    # class Meta:
    #     ordering = ['id']
