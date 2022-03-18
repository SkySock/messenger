from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import FileExtensionValidator
from django.db import models

from src.base.services import get_path_upload_profile_image, get_default_profile_image, validate_image_size


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('The given email address must be set')
        if not username:
            raise ValueError('The given username must be set')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    bio = models.TextField(max_length=2000, blank=True, default='')
    display_status = models.CharField(max_length=128, blank=True, default='')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(
        max_length=255,
        upload_to=get_path_upload_profile_image,
        null=True,
        blank=True,
        default=get_default_profile_image,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', ]), validate_image_size]
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Contact(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='owner')
    contact = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return f'У {self.user} есть контакт "{self.contact}"'
