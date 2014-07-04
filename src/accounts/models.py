# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    date_of_birth = models.DateField(verbose_name=u'Дата рождения', null=True, blank=True)

