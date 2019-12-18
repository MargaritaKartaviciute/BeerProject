from .models import *

from haversine import haversine, Unit
import numpy as np

class BreweriesService:
    def __init__(self):
        self.traveled_distance = 0
        self.home_lat = 0
        self.home_lon = 0
        self.maximum_distance = 2000
        self.brew_ids = []
        self.breweries = []

    def route(self, current_lat, current_long):
        self.home_lat = current_lat
        self.home_lon = current_long
        self.brew_ids = Geocodes.objects.values_list('id', flat=True)

        place = {
            'lat': self.home_lat,
            'lon': self.home_lon,
            'coordinate_id': -1,
            'name': "HOME",
            'distance': 0
        }
        self.breweries.append(place)
        self.__find_brewery(self.home_lat, self.home_lon)


    def __find_brewery(self, current_lat, current_long):

        possible_distances = []
        dist_coordinate_ids = []
        for id in self.brew_ids:

            coordinate = Geocodes.objects.get(id=id)
            if(current_long == coordinate.longitude and current_lat == coordinate.latitude):
                continue
            already_exist = False

            for brewery in self.breweries:
                if id == brewery['coordinate_id']:
                    already_exist = True
                    break
            if already_exist == False:

                distance = haversine((current_lat, current_long), (coordinate.latitude, coordinate.longitude), unit=Unit.KILOMETERS)

                if distance * 2 < self.maximum_distance and self.maximum_distance - self.traveled_distance > distance:
                    possible_distances.append(distance)
                    dist_coordinate_ids.append(id)

        if len(possible_distances) > 0:
            min_ind = np.array(possible_distances).argmin()
            next_coordinate = Geocodes.objects.get(id=dist_coordinate_ids[min_ind])

            distance_to_home = haversine((current_lat, current_long), (next_coordinate.latitude, next_coordinate.longitude))

            if (distance_to_home + possible_distances[min_ind] + self.traveled_distance <= self.maximum_distance):
                self.traveled_distance += possible_distances[min_ind]
                place = {
                    'lat': next_coordinate.latitude,
                    'lon': next_coordinate.longitude,
                    'coordinate_id': next_coordinate.id,
                    'name': Breweries.objects.get(id=next_coordinate.brewery_id).name,
                    'distance': possible_distances[min_ind]
                }
                self.breweries.append(place)

                self.__find_brewery(next_coordinate.latitude, next_coordinate.longitude)


    def __find_beer_types(self):
        pass






