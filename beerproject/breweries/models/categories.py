from django.db import models


class Categories(models.Model):
    cat_name = models.CharField(max_length=255, blank=True, null=True)
    last_mod = models.DateField()

    class Meta:
        managed = True
        db_table = 'categories'
        verbose_name_plural = "Categories"