from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categories, Styles, Beers, Breweries, Geocodes

admin.site.register(Categories)
admin.site.register(Styles)
admin.site.register(Beers)
admin.site.register(Breweries)
admin.site.register(Geocodes)
