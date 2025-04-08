from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User, UserPersonalInfo

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserPersonalInfo.objects.create(user=instance)