from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


'''    save_profile: This function is triggered every time a User instance is saved, '
       'whether it')s created for the first time or updated later. 
Its purpose is to ensure that the associated Profile instance is saved whenever the User is saved,
maintaining consistency between the User and Profile data.
sender: Identifies the model that triggered the signal (in this case, User).
instance: The specific instance of the model that was saved.
created: A boolean indicating if the instance was newly created.
**kwargs: Allows for handling additional keyword arguments that might be passed to the signal.
'''
''''create_profile: This function is specifically triggered when a new User instance is created (created=True). 
It's responsible for creating a corresponding Profile instance for the newly created User.

'''''
