from django.db import models
from django.contrib.gis.db import models
import uuid



# Head
class Head(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    age = models.BigIntegerField()
    sex = models.CharField(max_length=254)
    disability = models.CharField(max_length=254)
    disab_stat = models.CharField(max_length=254)
    learn_stat = models.CharField(max_length=254)
    tribe = models.CharField(max_length=254)
    death_stat = models.BigIntegerField()
    religion = models.CharField(max_length=254)
    mar_stat = models.CharField(max_length=254)
    employer = models.CharField(max_length=254)
    ipm = models.BigIntegerField()
    work_stat = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geom = models.MultiPointField(srid=4326)



class Watuka(models.Model):
    id = models.BigIntegerField(primary_key=True)
    area_name = models.CharField(max_length=80)
    area_id = models.BigIntegerField()
    area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)



class Child(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    age = models.BigIntegerField()
    sex = models.CharField(max_length=254)
    disability = models.CharField(max_length=254)
    disab_stat = models.CharField(max_length=254)
    learn_stat = models.CharField(max_length=254)
    tribe = models.CharField(max_length=254)
    religion = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geom = models.MultiPointField(srid=4326)





class Spouse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    age = models.BigIntegerField()
    sex = models.CharField(max_length=254)
    disability = models.CharField(max_length=254)
    disab_stat = models.CharField(max_length=254)
    learn_stat = models.CharField(max_length=254)
    tribe = models.CharField(max_length=254)
    death_stat = models.BigIntegerField()
    religion = models.CharField(max_length=254)
    mar_stat = models.CharField(max_length=254)
    employer = models.CharField(max_length=254)
    ipm = models.BigIntegerField()
    work_stat = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geom = models.MultiPointField(srid=4326)







class Population(models.Model):
    join_count = models.BigIntegerField()
    target_fid = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True)
    area_name = models.CharField(max_length=80)
    area_id = models.BigIntegerField()
    area = models.FloatField()
    name = models.CharField(max_length=254)
    age = models.BigIntegerField()
    sex = models.CharField(max_length=254)
    disability = models.CharField(max_length=254)
    disab_stat = models.CharField(max_length=254)
    learn_stat = models.CharField(max_length=254)
    tribe = models.CharField(max_length=254)
    death_stat = models.CharField(max_length=254)
    religion = models.CharField(max_length=254)
    mar_stat = models.CharField(max_length=254)
    employer = models.FloatField()
    ipm = models.CharField(max_length=254)
    work_stat = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)










   



