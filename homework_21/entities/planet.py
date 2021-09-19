from __future__ import annotations


class Planet:
    def __init__(
            self,
            name,
            rotation_period,
            orbital_period,
            diameter,
            climate,
            gravity,
            terrain,
            surface_water,
            population
    ):
        self.__name = name,
        self.__rotation_period = rotation_period,
        self.__orbital_period = orbital_period,
        self.__diameter = diameter,
        self.__climate = climate,
        self.__gravity = gravity,
        self.__terrain = terrain,
        self.__surface_water = surface_water,
        self.__population = population

    def __eq__(self, other: Planet):
        return self.__dict__ == other.__dict__
