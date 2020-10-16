from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

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
    return render(request,'squirrels/testview.html', context)

def detail(request, sighting_id):
    sighting = get_object_or_404(SquirrelDB, pk=sighting_id)

    context = {
            'sighting': sighting,
    }
    return render(request, 'squirrels/detail.html', context)


def update(request):
    return HttpResponse('updates page')

def add(request):
    return HttpResponse('add page')

def stats(request):
    return HttpResponse('stats page')
