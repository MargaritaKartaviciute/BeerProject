from django.db import models

from .breweries import Breweries


class Beers(models.Model):
    id = models.IntegerField(primary_key=True)
    brewery = models.ForeignKey(Breweries, models.DO_NOTHING)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'beers'
        verbose_name_plural = "Beers"