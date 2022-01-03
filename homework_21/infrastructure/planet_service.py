from requests import Response, get

from config_app import config


class PlanetService:
    def __init__(self):
        self.__planet_url = f"{config['base_url']}/planets"

    def get_planet(self, id_: int) -> Response:
        return get(f"{self.__planet_url}/{id_}")
