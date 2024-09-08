from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserInfoManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class UserInfo(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=25,
        unique=True,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9_]+$',
                message='Username must contain only letters, numbers, or underscores.'
            ),
            MinLengthValidator(4, message='Username must be at least 4 characters long.')
        ],
        error_messages={
            'unique': 'A user with this username already exists.'
        }
    )
    email = models.EmailField(
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(5, message='Email must be at least 5 characters long.')],
        error_messages={
            'unique': 'A user with this email address already exists.'
        }
    )
    phone = models.CharField(
        max_length=12,
        validators=[MinLengthValidator(10, message='Phone number must be at least 10 characters long.')],
        null=True,
        blank=True,
        unique=True,
        error_messages={
            'unique': 'A user with this phone number already exists.'
        }
    )
    password = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserInfoManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'userinfo'
