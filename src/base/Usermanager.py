from django.contrib.auth.models import BaseUserManager

class RUserManager(BaseUserManager):
        def create_user(self,email,DoB,name,Password=None):
                if email is None:
                        raise ValueError("user must have an email address")
                if name is None or DoB is None:
                        raise ValueError("user must have a name and Date of Birth")
                user =  self.model(email=self.normalize_email(email),name=name,DoB=DoB)
                user.set_password(Password)
                user.save(using=self._db)
                return user
        def create_supersuer(self,email,DoB,name,Password):
               user = self.create_user(email,DoB,name,Password)
               user.is_superuser = True
               user.save(using=self._db)
               return user