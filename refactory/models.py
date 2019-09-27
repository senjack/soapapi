from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone





# Create your models here.


class  RefactoryUserManager(BaseUserManager):
    
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    
    



class RefactoryUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    Primary_Contact= models.CharField(max_length=255,blank=True,null=True)
    Secondary_Contact= models.CharField(max_length=255,blank=True,null=True)
    # date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = RefactoryUserManager()


    def __str__(self):
        return self.email

    # @property
    # def token(self):
    #     """
    #     Allows us to get a user's token by calling `user.token` instead of
    #     `user.generate_jwt_token().

    #     The `@property` decorator above makes this possible. `token` is called
    #     a "dynamic property".
    #     """
    #     return self._generate_jwt_token()


    # def _generate_jwt_token(self):
    #     """
    #     Generates a JSON Web Token that stores this user's ID and has an expiry
    #     date set to 60 days into the future.
    #     """
    #     dt = datetime.now() + timedelta(days=60)

    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': int(dt.strftime('%s'))
    #     }, settings.SECRET_KEY, algorithm='HS256')

    #     return token.decode('utf-8')



class Administrator(RefactoryUser):
        User=models.OneToOneField(RefactoryUser,on_delete=models.CASCADE)
        Admin_id=models.AutoField(primary_key=True)
        
                
        Admin_Photo= models.CharField(max_length=255,blank=True,null=True)

        # created_at = models.DateTimeField(auto_now_add=True)
        # updated_at = models.DateTimeField(auto_now=True)
        

        def __str__(self):
            return self.email

        ordering = ('email')

class Staff(RefactoryUser):
        User=models.OneToOneField(Administrator,on_delete=models.CASCADE)
        Staff_id=models.AutoField(primary_key=True)
        
        Staff_Photo= models.CharField(max_length=255,blank=True,null=True)
        Admin_id=models.ForeignKey(Administrator,related_name='+', blank=True, on_delete=models.CASCADE,null=True)
        

        # created_at = models.DateTimeField(auto_now_add=True)
        # updated_at = models.DateTimeField(auto_now=True)
        

        def __str__(self):
            return self.email


class Applicant(RefactoryUser):
        User=models.OneToOneField(RefactoryUser,on_delete=models.CASCADE)
        applicant_id=models.AutoField(primary_key=True)

        Title=models.CharField(max_length=255,blank=True,null=True)
        applicant_Photo= models.CharField(max_length=255,blank=True,null=True)
        Gender= models.CharField(max_length=255,blank=True,null=True)
        DateofBirth=models.DateField(blank=True,null=True)
        Town_Residential= models.CharField(max_length=255,blank=True,null=True)
        Country= models.CharField(max_length=255,blank=True,null=True)
        Nationality= models.CharField(max_length=255,blank=True,null=True)
        # created_at = models.DateTimeField(auto_now_add=True)
        # updated_at = models.DateTimeField(auto_now=True)
        
        

        def __str__(self):
            return self.email






