from django.core.management import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = [
            {'name': 'moderators', 'description': 'Модераторы'}
        ]

        for group_data in groups:
            group, created = Group.objects.get_or_create(name=group_data['name'])
            if created:
                group.description = group_data['description']
                group.save()
