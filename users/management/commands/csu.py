from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание пользователей"""

    def handle(self, *args, **options):
        user = User.objects.create(email="admin@mail.ru")
        user.set_password("123qwe")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
