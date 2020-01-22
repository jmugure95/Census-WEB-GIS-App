from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from censuskenya import models as e_models


class headAdmin(LeafletGeoAdmin):
	list_display=['name','age',]
	list_filter= ['age']

class childAdmin(LeafletGeoAdmin):
	list_display=['name','sex','age','tribe','religion','disability']
	list_filter=['age']

class  SpouseAdmin(LeafletGeoAdmin):
	list_display=['name','sex','tribe','religion','disability']
	list_filter = ['age']

admin.site.register(e_models.Child,childAdmin)
admin.site.register(e_models.Head,headAdmin)
admin.site.register(e_models. Spouse, SpouseAdmin)

