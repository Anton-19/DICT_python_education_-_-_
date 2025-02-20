class Rabbit:
    def __init__(self, name, breed, weight, areal, color):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.areal = areal
        self.color = color
        self.size_category = self.determine_size()
        self.areal_category = self.determine_areal()

    def determine_size(self):
        if 5 <= self.weight <= 7:
            return "великих"
        elif 4 <= self.weight < 5:
            return "середніх"
        elif 3 <= self.weight < 4:
            return "маленьких"
        else:
            return "карликових"

    def determine_areal(self):
        areal_map = {
            "Північна та Південна Америка": "американських",
            "Європа та Азія": "євроазіатських",
            "Африка": "африканських",
            "Австралія": "австралійських"
        }
        return areal_map.get(self.areal, "невизначених")

    def get_description(self):
        message1 = f"Кролик {self.name} породи {self.breed}, що відноситься до {self.size_category} {self.areal_category} порід"
        message2 = f"важить {self.weight} кг і має забарвлення {self.color}"
        return f"{message1}. {message2}."


name = input("Введіть ім'я кролика:> ")
breed = input("Введіть породу кролика:> ")
weight = float(input("Введіть вагу кролика:> "))
areal = input(
    "Введіть ареал проживання кролика (доступні варіанти: Північна та Південна Америка, Європа та Азія, Африка, Австралія):> ")
color = input("Введіть забарвлення кролика:> ")

rabbit = Rabbit(name, breed, weight, areal, color)
print(rabbit.get_description())
