#Python file for exporting squirrel data from the Django SquirrelDB model to a CSV file
import csv
import os
import sys

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

class Command(BaseCommand):
    help = 'Export csv from Model database.'
	
    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        csvPath = options['path']

        Model = apps.get_model('squirrels', 'SquirrelDB')
        if not Model:
            raise CommandError("Model doesn't exist")

        field_names = [f.name for f in Model._meta.fields]

        csv_file = csvPath.replace('/','//')
        try:
            with open(csv_file,'w') as csvfile:
                filewriter = csv.writer(csvfile, delimiter = ',', lineterminator = '\n')
                filewriter.writerow(field_names[1:])
                
                for instance in Model.objects.all():
                    filewriter.writerow([(getattr(instance, f)) for f in field_names[1:]])
                    
        except IOError:
            print("I/O Error")

