from django.db import models
from .Usermanager import RUserManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class RUser(AbstractBaseUser):
    name = models.CharField(max_lenth=200)
    email = models.EmailField(unique=True,null=False)
    DoB = models.DateField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField(default=False)
    objects = RUserManager()
    USERNAME_FIELD =    'email'
    REQUIRED_FIELDS = ['name','DoB']

class RCustomer(RUser):
    pass