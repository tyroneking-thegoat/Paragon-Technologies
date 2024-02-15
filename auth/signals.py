from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from user_info.models import userInformation
from django.db.models.signals import pre_delete

#Create a new user info object to store user information alongside classes
@receiver(post_save, sender=User)
def create_user_info(instance, created, **kwargs):
    if created:
        user_info = userInformation.objects.create(
            username=instance.username,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            name=instance.username,
        )

# Deletes a userInformation object associated with a User when deleted
@receiver(pre_delete, sender=User)
def delete_user_info(sender, instance, **kwargs):
    try:
        user_info = userInformation.objects.get(name=instance.username)
        user_info.delete()
    except userInformation.DoesNotExist:
        pass  # Pass only if a userInformation object does not exist for the User being deleted