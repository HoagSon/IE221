from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer

@receiver (post_save, sender=User, dispath_uid= 'save_customer')

def save_customer(sender, instance, created, **kwargs):
    user = instance
    if created:
        return
    Customer.objects.create(user=instance)
    post_save.connect(save_customer, sender=user)