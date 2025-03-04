import random
import names


class Generator:
    breeds = ["Ангорський", "Рекс", "Фландр", "Каліфорнійський"]
    areals = ["Північна та Південна Америка", "Європа та Азія", "Африка", "Австралія"]
    colors = ["білий", "чорний", "сірий", "рудий", "плямистий"]

    def generate_rabbit(self) -> Rabbit:
        name = names.get_first_name()
        breed = random.choice(Generator.breeds)
        weight = round(random.uniform(2.0, 6.0), 1)  # Вага від 2 до 6 кг
        areal = random.choice(Generator.areals)
        color = random.choice(Generator.colors)
        return Rabbit(name, breed, weight, areal, color)

    def generate_1000(self) -> list:
        """Метод генерування 1000 об'єктів"""
        return [self.generate_rabbit() for _ in range(1000)]

    def generate_10_000(self) -> list:
        """Метод генерування 10 000 об'єктів"""
        return [self.generate_rabbit() for _ in range(10000)]


# Тестування
generator = Generator()
rabbit = generator.generate_rabbit()
print(repr(rabbit))

# Генерація списків
rabbits_1000 = generator.generate_1000()
rabbits_10000 = generator.generate_10_000()
