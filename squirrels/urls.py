from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'squirrels'

urlpatterns = [
        path('map/',views.map),
        path('sightings/',views.sightings),
        path('sightings/add/',views.add, name='add'),
        path('sightings/update/', views.update, name='update'),
        path('sightings/stats/',views.stats),
        path('sightings/<int:sighting_id>/',views.detail, name='detail'),
        ]
