from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(pre_save, sender=CustomUser)  # noqa
def update_user(sender, instance, **kwargs):
    """
    Updates user email verification status before saving
    """
    if instance.email_verified:
        instance.is_active = True
    else:
        instance.is_active = False
