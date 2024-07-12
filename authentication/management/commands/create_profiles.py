# authentication/management/commands/create_profiles.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from authentication.models import Profile


class Command(BaseCommand):
    help = 'Creates profile objects for existing users'

    def handle(self, *args, **options):
        users_without_profiles = User.objects.filter(profile__isnull=True)
        for user in users_without_profiles:
            Profile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Profile created for user: {user.username}'))
