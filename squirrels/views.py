from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from datetime import datetime

from django.db.models import Max

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
    sighting = get_object_or_404(SquirrelDB, pk=sighting_id)

    context = {
            'sighting': sighting,
    }
    return render(request, 'squirrels/detail.html', context)


def update(request):
    sighting = SquirrelDB()
    if request.method == "POST" and request.POST.get('submit_id') == "Update":
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
    if request.method == "POST":
        sighting = SquirrelDB()
        sighting.id = SquirrelDB.objects.aggregate(Max("id"))['id__max']
        sighting.sq_id = request.POST.get('sighting_sq_id')
        sighting.Shift = request.POST.get('Shift_id')
        sighting.X = request.POST.get('long_id')
        sighting.Y = request.POST.get('lat_id')
        sighting.Lat_long = "POINT (%s %s)" % (sighting.Y, sighting.X)
        sighting.Date = datetime.strptime(request.POST.get('Date_id'), "%b. %d, %Y")
        sighting.Age = request.POST.get('Age_id')
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
        context = {
            'sighting': sighting, "status": "Saved"
        }
        return render(request, 'squirrels/confirm.html', context)
    else:
        sighting = SquirrelDB()
    context = {
            'sighting': sighting,
    }

    return render(request, 'squirrels/add.html', context)


def stats(request):
    return HttpResponse('stats page')
