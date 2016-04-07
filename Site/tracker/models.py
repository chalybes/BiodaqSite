from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=255, blank=True)
    PSC = models.CharField(max_length=255)
    mouse = models.CharField(max_length=255, blank=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    # user = models.OneToOneField(User, blank=True, null=True)


