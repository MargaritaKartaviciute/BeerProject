from breweries.models import *
import time

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
        self.beer_types = set()
        self.execution_time = 0
        self.distance_to_home = 0


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

        start_time = time.time()

        self.__find_brewery(self.home_lat, self.home_lon)

        place = {
            'lat': self.home_lat,
            'lon': self.home_lon,
            'coordinate_id': -1,
            'name': "HOME",
            'distance': self.distance_to_home
        }
        self.breweries.append(place)

        self.execution_time = time.time() - start_time


    def __find_brewery(self, current_lat, current_long):

        possible_distances = []
        dist_coordinate_ids = []
        for id in self.brew_ids:
            coordinate = Geocodes.objects.get(id=id)
            if(current_long == coordinate.longitude and current_lat == coordinate.latitude):
                continue

            if self.__check_if_exists(id) == False:
                distance = haversine((current_lat, current_long), (coordinate.latitude, coordinate.longitude), unit=Unit.KILOMETERS)

                if ((distance * 2 < self.maximum_distance) and (self.maximum_distance - self.traveled_distance > distance)):
                    possible_distances.append(distance)
                    dist_coordinate_ids.append(id)

        if len(possible_distances) > 0:
            min_ind = np.array(possible_distances).argmin()
            next_coordinate = Geocodes.objects.get(id=dist_coordinate_ids[min_ind])

            distance_to_home = haversine((self.home_lat, self.home_lon), (next_coordinate.latitude, next_coordinate.longitude), unit=Unit.KILOMETERS)

            if ((distance_to_home + possible_distances[min_ind] + self.traveled_distance) <= self.maximum_distance):
                self.distance_to_home = distance_to_home
                self.traveled_distance += possible_distances[min_ind]

                self.__add_brewery_to_list(next_coordinate, possible_distances[min_ind])
                self.__add_beer_types(next_coordinate)

                self.__find_brewery(next_coordinate.latitude, next_coordinate.longitude)

    def __find_beer_types(self, id):
        return Beers.objects.filter(brewery_id=id)

    def __add_brewery_to_list(self, next_coordinate, distance):
        place = {
            'lat': next_coordinate.latitude,
            'lon': next_coordinate.longitude,
            'coordinate_id': next_coordinate.id,
            'name': Breweries.objects.get(id=next_coordinate.brewery_id).name,
            'distance': distance
        }
        self.breweries.append(place)

    def __check_if_exists(self, id):
        already_exist = False

        for brewery in self.breweries:
            if id == brewery['coordinate_id']:
                already_exist = True
                break
        return already_exist

    def __add_beer_types(self, next_coordinate):
        beer_types = self.__find_beer_types(next_coordinate.brewery_id)
        for beer in beer_types:
            self.beer_types.add(beer.name)









