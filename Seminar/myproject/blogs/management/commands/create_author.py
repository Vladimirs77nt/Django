from datetime import date
import random
from django.core.management.base import BaseCommand
from blogs.models import Author
import faker    # генерация фейковых имен и фамилий
from transliterate import translit  # транлирования русских букв в латиницу

fake = faker.Faker('ru_RU')

class Command(BaseCommand):
    help = "Create Author"

    def handle(self, *args, **kwargs):
        random_name=fake.first_name()
        random_surname=fake.last_name()
        name_lat = f"{random_surname}_{random_name}"
        random_email=f'{translit(name_lat, language_code="ru", reversed=True)}_{random.randint(100,1000)}@mail.ru'
        random_biography=f'Биография {random.randint(10000,1000000)}'
        birthday = date(year=random.randint(1950,2005), month=random.randint(1,12), day=random.randint(1,30))
        author = Author(name=random_name,
                        surname=random_surname,
                        email=random_email,
                        biography=random_biography,
                        birthday=birthday)
        author.save()
        self.stdout.write(f'Create author: {author}')