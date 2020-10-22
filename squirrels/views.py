from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from datetime import datetime

from django.db.models import Max, Count

from .models import SquirrelDB


def map(request):
    sightings = SquirrelDB.objects.all().filter(Primary_color = 'Black')
    context = {
            'sightings': sightings,
    }
    return render(request, 'squirrels/map.html', context)


def sightings(request):
    sightings = SquirrelDB.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request,'squirrels/sightings.html', context)


def detail(request, sighting_id):
    # retrieve the selected object's details, and provides an option to update the entries.

    sighting = get_object_or_404(SquirrelDB, pk=sighting_id)


    context = {
            'sighting': sighting,
    }
    return render(request, 'squirrels/detail.html', context)


def update(request):
    # check if it is GET or POST
    if request.method == "POST" and request.POST.get('submit_id') == "Update":
        sighting_id = request.POST.get('sighting_id')
        sighting = get_object_or_404(SquirrelDB, pk=sighting_id)
        sighting.Shift = request.POST.get('Shift_id')
        sighting.X = request.POST.get('long_id')
        sighting.Y = request.POST.get('lat_id')
        sighting.Lat_long = "POINT (%s %s)" % (sighting.Y, sighting.X)
        sighting.Date = datetime.strptime(request.POST.get('Date_id'), "%b. %d, %Y")
        sighting.Age = request.POST.get('Age_id')
        sighting.save()
    context = {
        'sighting': sighting, "status": "Updated"
    }
    return render(request, 'squirrels/confirm.html', context)


def add(request):
    if request.method == "POST" and request.POST.get('submit_id') == "Save":
        if len(request.POST.get('Date_id')) > 0 and "." in request.POST.get('Date_id') \
                and "," in request.POST.get('Date_id') and len(request.POST.get('sighting_sq_id')) > 0\
                and len(request.POST.get('Shift_id')) > 0 and len(request.POST.get('long_id')) > 0 \
                and len(request.POST.get('lat_id')) > 0:
            sighting = SquirrelDB()
            sighting.id = SquirrelDB.objects.aggregate(Max("id"))['id__max']
            sighting.sq_id = request.POST.get('sighting_sq_id')
            sighting.Shift = request.POST.get('Shift_id')
            sighting.X = request.POST.get('long_id')
            sighting.Y = request.POST.get('lat_id')
            sighting.Lat_long = "POINT (%s %s)" % (sighting.Y, sighting.X)
            try:
                # parse the date with given format
                sighting.Date = datetime.strptime(request.POST.get('Date_id'), "%b. %d, %Y")
            except Exception as e:
                # date parsing fails due to absence of space in between
                sighting.Date = datetime.strptime(request.POST.get('Date_id'), "%b.%d, %Y")
            except:
                # Another exception - date parsing fails due to absence of space in between
                sighting.Date = datetime.strptime(request.POST.get('Date_id'), "%b.%d,%Y")
            sighting.Age = request.POST.get('Age_id')
            # set all other options to random values to make sure that the data is saved.
            sighting.Running = True
            sighting.Chasing = True
            sighting.Climbing = True
            sighting.Eating = False
            sighting.Foraging = False
            sighting.Kuks = False
            sighting.Quass = False
            sighting.Moans = False
            sighting.Approaches = False
            sighting.Tail_flag = False
            sighting.Tail_twitch = False
            sighting.Indifferent = False
            sighting.Runs_from = False
            sighting.save()

            # Redirects to confirmation page
            context = {
                'sighting': sighting, "status": "Saved"
            }
        else:
            context = {
                'sighting': "", "status": "Error"
            }
        return render(request, 'squirrels/confirm.html', context)
    else:
        sighting = SquirrelDB()
    context = {
            'sighting': sighting,
    }
    # if it is a new entry request, then page will be redirected to add entry page.
    return render(request, 'squirrels/add.html', context)


def stats(request):
    shift_count = SquirrelDB.objects.all().values('Shift').annotate(total=Count('Shift'))
    date_count = SquirrelDB.objects.all().values('Date').annotate(total=Count('Date'))
    age_count = SquirrelDB.objects.all().values('Age').annotate(total=Count('Age'))
    running = SquirrelDB.objects.all().values('Running').annotate(total=Count('Running'))
    eating = SquirrelDB.objects.all().values('Eating').annotate(total=Count('Eating'))
    context = {
            'shift': shift_count, 'date': date_count, 'age': age_count, 'running': running, 'eating': eating
    }
    return render(request, 'squirrels/stats.html', context)
