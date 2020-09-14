from django.db import models
from django.contrib.gis.db import models
# Create your models here.


class Departments(models.Model):
    code = models.CharField(max_length=254)
    nom = models.CharField(max_length=254)
    area = models.FloatField()
    population = models.FloatField()
    pop_den = models.FloatField()
    tot_death_field = models.BigIntegerField()
    tot_infect = models.BigIntegerField()
    death_rate = models.FloatField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.nom


# Auto-generated `LayerMapping` dictionary for Departments model
departments_mapping = {
    'code': 'code',
    'nom': 'nom',
    'area': 'area',
    'population': 'population',
    'pop_den': 'pop_den',
    'tot_death_field': 'tot_death_',
    'tot_infect': 'tot_infect',
    'death_rate': 'death_rate',
    'lon': 'lon',
    'lat': 'lat',
    'geom': 'MULTIPOLYGON',
}
