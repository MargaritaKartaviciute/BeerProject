from django.db import models

from .categories import Categories


class Styles(models.Model):
    cat = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    style_name = models.CharField(max_length=255)
    last_mod = models.DateField()

    class Meta:
        managed = True
        db_table = 'styles'
        verbose_name_plural = "Styles"
