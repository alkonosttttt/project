from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser, UserManager):

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
