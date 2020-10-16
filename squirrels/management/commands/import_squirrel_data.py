#Python file for importing squirrel data from a CSV into the Django database
import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

class Command(BaseCommand):
    args = 'Model.csv'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        csvPath = options['path']
        if not os.path.exists(csvPath):
            raise CommandError("%s does not exist." %csvPath)

        model, _ = os.path.splitext(os.path.basename(csvPath))
        Model = apps.get_model('squirrels', 'SquirrelDB')
        if not Model:
            raise CommandError("Model does not exist.")

        model_fields = [f.name for f in Model._meta.fields]
        fields_name = []
        with open(csvPath,'r') as csvFile:
            reader = csv.reader(csvFile, delimiter=',',quotechar="\"")
            fields_name = next(reader)
            for i, _ in enumerate(fields_name):
                if fields_name[i] == "X":
                    fields_name[i] = "X"
                elif fields_name[i] == "Y":
                    fields_name[i] = "Y"
                elif fields_name[i] == "Unique Squirrel ID":
                    fields_name[i] = "sq_id"
                elif fields_name[i] == "Hectare":
                    fields_name[i] = "Hect"
                elif fields_name[i] == "Shift":
                    fields_name[i] = "Shift"
                elif fields_name[i] == "Date":
                    fields_name[i] = "Date"
                elif fields_name[i] == "Hectare Squirrel Number":
                    fields_name[i] = "Hect_sq_num"
                elif fields_name[i] == "Age":
                    fields_name[i] = "Age"
                elif fields_name[i] == "Primary Fur Color":
                    fields_name[i] = "Primary_color"
                elif fields_name[i] == "Highlight Fur Color":
                    fields_name[i] = "Highlight_color"
                elif fields_name[i] == "Combination of Primary and Highlight Color":
                    fields_name[i] = "Combo"
                elif fields_name[i] == "Color notes":
                    fields_name[i] = "Color_notes"
                elif fields_name[i] == "Location":
                    fields_name[i] = "Location"
                elif fields_name[i] == "Above Ground Sighter Measurement":
                    fields_name[i] = "Above_measure"
                elif fields_name[i] == "Specific Location":
                    fields_name[i] = "Specific_loc"
                elif fields_name[i] == "Running":
                    fields_name[i] = "Running"
                elif fields_name[i] == "Chasing":
                    fields_name[i] = "Chasing"
                elif fields_name[i] == "Climbing":
                    fields_name[i] = "Climbing"
                elif fields_name[i] == "Eating":
                    fields_name[i] = "Eating"
                elif fields_name[i] == "Foraging":
                    fields_name[i] = "Foraging"
                elif fields_name[i] == "Other Activities":
                    fields_name[i] = "Other_act"
                elif fields_name[i] == "Kuks":
                    fields_name[i] = "Kuks"
                elif fields_name[i] == "Quaas":
                    fields_name[i] = "Quass"
                elif fields_name[i] == "Moans":
                    fields_name[i] = "Moans"
                elif fields_name[i] == "Tail flags":
                    fields_name[i] = "Tail_flag"
                elif fields_name[i] == "Tail twitches":
                    fields_name[i] = "Tail_twitch"
                elif fields_name[i] == "Approaches":
                    fields_name[i] = "Approaches"
                elif fields_name[i] == "Indifferent":
                    fields_name[i] = "Indifferent"
                elif fields_name[i] == "Runs from":
                    fields_name[i] = "Runs_from"
                elif fields_name[i] == "Other Interactions":
                    fields_name[i] = "Other_interactions"
                elif fields_name[i] == "Lat/Long":
                    fields_name[i] = "Lat_long"
                else:
                    raise CommandError ("%s field does not exist in %s Model" %(fields_name[i], Model))

            for row in reader:
            
                row_dict = {}
                for i, field in enumerate(row):
                    if fields_name[i] == "Date":
                        field = field[4:]+'-'+field[0:2]+'-'+field[2:4]
                    if field.lower() == "true" or field.lower() == "false":
                        field = (field.lower()).capitalize()
                     
                    row_dict[fields_name[i]] = field

                obj, created = Model.objects.update_or_create(
                        Lat_long = row_dict['Lat_long'],
                        sq_id = row_dict['sq_id'],
                        defaults = row_dict,
                        )
