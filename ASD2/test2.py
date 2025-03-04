import bisect
import names
import random

class Rabbit:
    def __init__(self, name: str, breed: str, weight: float, areal: str, color: str) -> None:
        self.name: str = name
        self.breed: str = breed
        self.weight: float = weight
        self.areal: str = areal
        self.color: str = color
        self.size_category: str = self.determine_size()
        self.areal_category: str = self.determine_areal()

    def determine_size(self) -> str:
        categories = ["карликових", "маленьких", "середніх", "великих"]
        thresholds = [3, 4, 5]  # Межі для категорій
        index = bisect.bisect_left(thresholds, self.weight)
        return categories[index]

    def determine_areal(self) -> str:
        areal_map: dict[str, str] = {
            "Північна та Південна Америка": "американських",
            "Європа та Азія": "євроазіатських",
            "Африка": "африканських",
            "Австралія": "австралійських"
        }
        return areal_map.get(self.areal, "невизначених (неправильний ареал)")

    def get_description(self) -> str:
        return (f"Кролик {self.name} породи {self.breed}, що відноситься до {self.size_category} "
                f"{self.areal_category} порід, важить {self.weight} кг і має забарвлення {self.color}.")

    def __repr__(self) -> str:
        return (f"Rabbit(name={self.name!r}, breed={self.breed!r}, weight={self.weight}, "
                f"areal={self.areal!r}, color={self.color!r})")

class Generator:
    breeds = ["Ангорський", "Рекс", "Фландр", "Карликовий"]
    areals = ["Північна та Південна Америка", "Європа та Азія", "Африка", "Австралія"]
    colors = ["білий", "чорний", "коричневий", "сивий"]

    def generate_rabbit(self) -> Rabbit:
        name = names.get_first_name()
        breed = random.choice(self.breeds)
        weight = round(random.uniform(2.0, 6.0), 1)
        areal = random.choice(self.areals)
        color = random.choice(self.colors)
        return Rabbit(name, breed, weight, areal, color)

    def generate_1000(self) -> list:
        """Метод генерування 1000 об'єктів"""
        return [self.generate_rabbit() for _ in range(1000)]

    def generate_10_000(self) -> list:
        """Метод генерування 10 000 об'єктів"""
        return [self.generate_rabbit() for _ in range(10000)]