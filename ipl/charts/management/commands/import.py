import csv

from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import transaction

from ipl.charts.models import Match


# This is the class to create command for importing dataset.
class Command(BaseCommand):

    help = "This is used to import data from csv file to a Model"

    def add_arguments(self, parser):
        
        parser.add_argument('-app', type=str, help='App Name for the Model')
        parser.add_argument('-model', type=str, help='Model Name')
        parser.add_argument('-path', type=str, help='path for CSV file')

    def handle(self, *args, **options):

        # Get the model
        _model = apps.get_model(options['app'], options['model'])

        # get the file path
        file_path = options['path']

        # Do all the stuff using atomic transaction
        with transaction.atomic():

            with open(file_path, 'r') as file:
                reader = csv.reader(file)

                header = next(reader)
                
                for row in reader:

                    dictionary = {key: value for key, value in zip(header, row)}

                    # Model is Delivery
                    if options['model'] == 'Delivery':
                        obj = Match.objects.get(pk = dictionary['match_id'])
                        dictionary['match'] = obj

                    obj = _model(**dictionary)
                    obj.save()