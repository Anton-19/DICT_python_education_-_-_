import pytest
from Rabbit_Generator import Rabbit, Generator

def test_rabbit_creation():
    rabbit = Rabbit("Білий", "Ангорський", 3.5, "Європа та Азія", "білий")
    assert isinstance(rabbit, Rabbit)
    assert rabbit.name == "Білий"
    assert rabbit.breed == "Ангорський"
    assert rabbit.weight == 3.5
    assert rabbit.areal == "Європа та Азія"
    assert rabbit.color == "білий"

def test_rabbit_description():
    rabbit = Rabbit("Чорний", "Рекс", 4.2, "Африка", "чорний")
    description = rabbit.get_description()
    assert "Кролик Чорний породи Рекс" in description
    assert "важить 4.2 кг" in description
    assert "ареал проживання: Африка" in description
    assert "забарвлення: чорний" in description

def test_generator_rabbit():
    generator = Generator()
    rabbit = generator.generate_rabbit()
    assert isinstance(rabbit, Rabbit)
    assert rabbit.breed in Generator.breeds
    assert rabbit.areal in Generator.areals
    assert rabbit.color in Generator.colors
    assert 2.0 <= rabbit.weight <= 6.0

def test_generate_1000():
    generator = Generator()
    rabbits = generator.generate_1000()
    assert len(rabbits) == 1000
    assert all(isinstance(r, Rabbit) for r in rabbits)

def test_generate_10_000():
    generator = Generator()
    rabbits = generator.generate_10_000()
    assert len(rabbits) == 10000
    assert all(isinstance(r, Rabbit) for r in rabbits)
