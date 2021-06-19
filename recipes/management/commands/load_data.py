import csv
from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Imports data into the ingredients model'

    def handle(self, *args, **options):
        with open('recipes/data/ingredients.csv') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                title, dimension = row
                Ingredient.objects.get_or_create(title=title, dimension=dimension)
