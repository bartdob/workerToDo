import random
import factory
from todo import models
from faker import Faker
fake = Faker()


class WorkerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Worker

    forename = factory.Faker.first_name(80)
    surname = factory.Faker.last_name(80)
    date_od_birth = factory.Faker.date_object()
    age = random.randint(1, 1000)
    content = factory.Faker.text(70)
    date = factory.Faker.date_object()
