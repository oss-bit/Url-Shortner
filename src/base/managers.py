from django.contrib.auth.models import BaseUserManager

class RUserManager(BaseUserManager):
    def create_user(self, email, DoB, password):
        if not email:
            raise ValueError('User must have an email address')
        if not DoB:
            raise ValueError('Date of Birth must be supplied to create a new user')
        if not password:
            raise ValueError('Password must be supplied to create a new user')
        user = self.model(
            email=self.normalize_email(email),
            DoB=DoB
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, DoB, password):
        user = self.create_user(email=email, DoB=DoB, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user