import os
from django.contrib.gis.utils import LayerMapping
from .models import Watuka,Head,Child,Spouse,Population

watuka_mapping = {
    'id': 'id',
    'area_name': 'Area_Name',
    'area_id': 'Area_Id',
    'area': 'Area',
    'geom': 'MULTIPOLYGON',
}

watuka_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Watuka.shp'),
)

def run(verbose=True):
    lm = LayerMapping(Watuka, watuka_shp, watuka_mapping,transform=True,encoding='iso-8859-1',)
    lm.save(strict=True, verbose=verbose)

head_mapping = {
    'id': 'id',
    'name': 'name',
    'age': 'age',
    'sex': 'sex',
    'disability': 'disability',
    'disab_stat': 'disab_stat',
    'learn_stat': 'learn_stat',
    'tribe': 'tribe',
    'death_stat': 'death_stat',
    'religion': 'religion',
    'mar_stat': 'mar_stat',
    'employer': 'employer',
    'ipm': 'Ipm',
    'work_stat': 'work_stat',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'geom': 'MULTIPOINT',
}


head_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Head.shp'),
)

def run1(verbose=True):
    lm = LayerMapping(Head, head_shp, head_mapping,transform=True,encoding='iso-8859-1',)
    lm.save(strict=True, verbose=verbose)

child_mapping = {
    'id': 'id',
    'name': 'name',
    'age': 'age',
    'sex': 'sex',
    'disability': 'disability',
    'disab_stat': 'disab_stat',
    'learn_stat': 'learn_stat',
    'tribe': 'tribe',
    'religion': 'religion',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'geom': 'MULTIPOINT',
}




child_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Child.shp'),
)

def run2(verbose=True):
    lm = LayerMapping(Child, child_shp, child_mapping,transform=True,encoding='iso-8859-1',)
    lm.save(strict=True, verbose=verbose)

spouse_mapping = {
    'id': 'id',
    'name': 'name',
    'age': 'age',
    'sex': 'sex',
    'disability': 'disability',
    'disab_stat': 'disab_stat',
    'learn_stat': 'learn_stat',
    'tribe': 'tribe',
    'death_stat': 'death_stat',
    'religion': 'religion',
    'mar_stat': 'mar_stat',
    'employer': 'employer',
    'ipm': 'Ipm',
    'work_stat': 'work_stat',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'geom': 'MULTIPOINT',
}




spouse_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Spouse.shp'),
)

def run3(verbose=True):
    lm = LayerMapping(Spouse, spouse_shp, spouse_mapping,transform=True,encoding='iso-8859-1',)
    lm.save(strict=True, verbose=verbose)


population_mapping = {
    'join_count': 'Join_Count',
    'target_fid': 'TARGET_FID',
    'id': 'id',
    'area_name': 'Area_Name',
    'area_id': 'Area_Id',
    'area': 'Area',
    'name': 'name',
    'age': 'age',
    'sex': 'sex',
    'disability': 'disability',
    'disab_stat': 'disab_stat',
    'learn_stat': 'learn_stat',
    'tribe': 'tribe',
    'death_stat': 'death_stat',
    'religion': 'religion',
    'mar_stat': 'mar_stat',
    'employer': 'employer',
    'ipm': 'Ipm',
    'work_stat': 'work_stat',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'geom': 'MULTIPOLYGON',
}

population_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Pop join.shp'),
)

def run4(verbose=True):
    lm = LayerMapping(Population, population_shp, population_mapping,transform=True,encoding='iso-8859-1',)
    lm.save(strict=True, verbose=verbose)
