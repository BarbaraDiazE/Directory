# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

# from django.utils.crypto import get_random_string
from faker import Faker
from directory.models import Programers


class Command(BaseCommand):
    help = "create random users"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of users to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        fake = Faker()
        for i in range(total):
            Programers.objects.create(
                name=fake.name(), email=fake.email(), position="Software engineer",
            )

