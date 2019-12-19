from django.db import models

from .breweries import Breweries


class Geocodes(models.Model):
    id = models.IntegerField(primary_key=True)
    brewery = models.ForeignKey(Breweries, models.DO_NOTHING)
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'geocodes'
        verbose_name_plural = "Geocodes"