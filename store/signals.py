from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from store.models import Customer

@receiver(post_save,sender=User)
def create_customer(sender, instance, created, **kwargs):
	if created:
		Customer.objects.create(user=instance, email=instance.email)

@receiver(post_save,sender=User)
def save_customer(sender, instance, **kwargs):
	instance.customer.save()
