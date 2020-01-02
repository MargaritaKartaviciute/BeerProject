# from .models import Geocodes
from django.shortcuts import render

from django.views.generic import  TemplateView
from .forms import BreweriesForm
from .services import BreweriesService


class BreweriesView(TemplateView):
    template_name = 'index.html'
    post_template = 'post.html'
    _service = BreweriesService()

    def get(self, request):

        form = BreweriesForm()
        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = BreweriesForm(request.POST)
        if form.is_valid():
            longitude = form.cleaned_data['longitude']
            latitude = form.cleaned_data['latitude']
            self._service.route(latitude, longitude)
            results = self._service.breweries
            all_distance = self._service.traveled_distance
            beers = self._service.beer_types
            distance_to_home = self._service.distance_to_home
            execution_time = self._service.execution_time
            form = BreweriesForm()

        context = {
            'longitude': longitude,
            'latitude': latitude,
            'form': form,
            'results': results,
            'total_distance': all_distance + distance_to_home,
            'beers': beers,
            'distance_to_home': distance_to_home,
            'execution_time': execution_time
        }
        return render(request, self.post_template, context)
