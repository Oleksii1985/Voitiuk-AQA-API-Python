"""
Выбрать на ваше усмотрение публичный апи для проекта по апи тестам
Организовать базовую структуру каталогов в проекте
Создать пару тестов и кофтест с фикстурами для выбранного публичного апи
"""
from entities.planet import Planet


def test_check_response_of_planet_01(planet_service, first_planet):
    response = planet_service.get_planet(1)
    actual_planet = Planet(
        response.json()["name"],
        response.json()["rotation_period"],
        response.json()["orbital_period"],
        response.json()["diameter"],
        response.json()["climate"],
        response.json()["gravity"],
        response.json()["terrain"],
        response.json()["surface_water"],
        response.json()["population"]
    )
    assert actual_planet == first_planet


def test_check_response_of_planet_02(planet_service, second_planet):
    response = planet_service.get_planet(2)
    actual_planet = Planet(
        response.json()["name"],
        response.json()["rotation_period"],
        response.json()["orbital_period"],
        response.json()["diameter"],
        response.json()["climate"],
        response.json()["gravity"],
        response.json()["terrain"],
        response.json()["surface_water"],
        response.json()["population"]
    )
    assert actual_planet == second_planet