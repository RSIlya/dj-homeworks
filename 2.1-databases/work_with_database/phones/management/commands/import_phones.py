import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    help = 'Import data from csv file to DB'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            try:
                Phone.objects.get(name=phone['name'])
            except Phone.DoesNotExist:
                print(f"Добавление в базу данные о {phone['name']}")
                Phone.objects.create(
                    name=phone['name'],
                    image=phone['image'],
                    price=phone['price'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug=slugify(phone['name'])
                )
