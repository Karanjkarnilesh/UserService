
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class USERS(models.Model):
     userID = models.IntegerField(primary_key=True)
     UserName = models.CharField(max_length=125),
     Email = models.CharField(max_length=124,null=True)
     Phone = models.IntegerField()
     Password  = models.CharField(max_length=255)