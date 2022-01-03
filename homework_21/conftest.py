import pytest

from entities.planet import Planet
from infrastructure.planet_service import PlanetService


@pytest.fixture(scope="session")
def planet_service() -> PlanetService:
    yield PlanetService()


@pytest.fixture
def first_planet() -> Planet:
    yield Planet(
        name="Tatooine",
        rotation_period="23",
        orbital_period="304",
        diameter="10465",
        climate="arid",
        gravity="1 standard",
        terrain="desert",
        surface_water="1",
        population="200000"
    )


@pytest.fixture
def second_planet() -> Planet:
    yield Planet(
        name="Alderaan",
        rotation_period="24",
        orbital_period="364",
        diameter="12500",
        climate="temperate",
        gravity="1 standard",
        terrain="grasslands, mountains",
        surface_water="40",
        population="2000000000"
    )
