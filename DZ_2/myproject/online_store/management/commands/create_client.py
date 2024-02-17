from datetime import date
import random
from django.core.management.base import BaseCommand
from online_store.models import Client
import faker    # генерация фейковых имен и фамилий
from transliterate import translit  # транлирования русских букв в латиницу

fake = faker.Faker('ru_RU')

class Command(BaseCommand):
    help = "Create Client"

    def handle(self, *args, **kwargs):
        random_name=fake.name()
        # random_email=f'{translit(random_name, language_code="ru", reversed=True)}_{random.randint(100,1000)}@mail.ru'
        random_email=fake.ascii_free_email()
        telephone = fake.phone_number()
        address=fake.address()
        password=fake.password()
        birthday = date(year=random.randint(1950,2005), month=random.randint(1,12), day=random.randint(1,30))
        author = Client(name=random_name,
                        surname=random_surname,
                        email=random_email,
                        biography=random_biography,
                        birthday=birthday,
                        full_name=full_name)
        author.save()
        self.stdout.write(f'Create author: {author}')

    
name = models.CharField(max_length=100)
email = models.CharField(max_length=32)
telephone = models.EmailField()
password = models.CharField(max_length=12)
address = models.CharField(max_length=32)
date_reg = models.DateField()