from censuskenya import models as c_models
from rest_framework import serializers

class HeadSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = c_models.Head
	 	fields = [
	 		'id',
	 		'name',
	 		'age',
	 		'sex',
	 		'disability',
	 		'disab_stat',
	 		'learn_stat',
	 		'tribe',
	 		'death_stat',
	 		'religion',
	 		'mar_stat',
	 		'employer',
	 		'ipm',
	 		'work_stat',
	 		'latitude',
	 		'longitude',
	 		'geom'
	 	]


class SpouseSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = c_models.Spouse
	 	fields = [
	 		'id',
	 		'name',
	 		'age',
	 		'sex',
	 		'disability',
	 		'disab_stat',
	 		'learn_stat',
	 		'tribe',
	 		'death_stat',
	 		'religion',
	 		'mar_stat',
	 		'employer',
	 		'ipm',
	 		'work_stat',
	 		'latitude',
	 		'longitude',
	 		'geom'
	 	]

class ChildSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = c_models.Child
	 	fields = [
	 		'id',
	 		'name',
	 		'age',
	 		'sex',
	 		'disability',
	 		'disab_stat',
	 		'learn_stat',
	 		'tribe',
	 		'religion',
	 		'latitude',
	 		'longitude',
	 		'geom'
	 	]
class WatukaSerializer(serializers.ModelSerializer):
	class Meta:
		model=c_models.Watuka
		fields =[
		'id',
		'area_name',
		'area_id',
		'area',
		'geom'
		]

