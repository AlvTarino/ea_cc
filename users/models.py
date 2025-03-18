from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.urls import reverse
from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    objects = CustomUserManager()
    is_active = models.BooleanField(default=True, verbose_name='Active Status')
    is_staff = models.BooleanField(default=False, verbose_name='Staff Status')
    is_superuser = models.BooleanField(
        default=False, verbose_name='Superuser Status'
    )
    phone = models.CharField(max_length=20, blank=True)
    shipping_address = models.TextField(blank=True)
    billing_address = models.TextField(blank=True)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        # Automatically promote to staff/superuser
        if self.is_superuser:
            self.is_staff = True
            self.is_active = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'username': self.username})

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def has_shipping_address(self):
        return self.shipping_address != ''

    def has_billing_address(self):
        return self.billing_address != ''

    def has_email_verified(self):
        return self.email_verified

    def has_phone(self):
        return self.phone != ''
