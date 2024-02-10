from django.db import models
from .managers import RUserManager
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class RUser(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    DoB = models.DateField()
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = RUserManager()

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['DoB']
    def __str__(self):
        return self.email
    def has_module_perms(self, app_label):
        return True
    def has_perm(self, perm, obj=None):
        return True
    class Meta:
        ordering = ['-email']

class Link(models.Model):
    user = models.ForeignKey(RUser,on_delete=models.CASCADE)
    original_url = models.URLField()
    link_id = models.PositiveBigIntegerField()
    