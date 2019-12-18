from .models import Geocodes
from django.shortcuts import render

from django.views.generic import  TemplateView
from .forms import BreweriesForm
from .services import BreweriesService


class BreweriesView(TemplateView):
    template_name = 'index.html'
    _service = BreweriesService()

    def get(self, request):

        # ReadData.read_csv_data()
        coordinates = Geocodes.objects.all()
        form = BreweriesForm()
        context = {
            'coordinates': coordinates,
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
            form = BreweriesForm()

        context = {
            'longitude': longitude,
            'latitude': latitude,
            'form': form,
            'results': results
        }
        return render(request, self.template_name, context)
