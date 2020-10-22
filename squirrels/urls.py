from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'squirrels'

urlpatterns = [
        path('map/',views.map),
        path('',views.sightings),
        path('sightings/', views.sightings, name='view'),
        path('sightings/add/',views.add, name='add'),
        path('sightings/update/', views.update, name='update'),
        path('sightings/stats/', views.stats, name='stats'),
        path('sightings/<int:sighting_id>/', views.detail, name='detail'),
        ]
