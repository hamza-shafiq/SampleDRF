import re
from django.db import models
from .user_manager import UserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """
    Updated User Model
    """
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True,
                             error_messages={'unique': "This phone number has already been registered."})
    email = models.EmailField(max_length=255, unique=True,
                              error_messages={'unique': "This email has already been registered."})
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    activation_key = models.CharField(max_length=50, null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    token_expire = models.DateTimeField(_('token expire'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['phone']),
            models.Index(fields=['created_at'])
        ]

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def clean(self):
        if len(self.password) < 8:
            raise ValidationError("Password should be of minimum 8 characters")

        if re.search('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=]).*$', self.password) is None:
            raise ValidationError("Password should contain 1 numeric, 1 special character and 1 Capital letter.")


class Dispatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    short_code = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_code
