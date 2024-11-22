class CoffeeMachine:
    def __init__(self):
        # ресурсів кавомашини з початку
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = "choosing_action"

    def show_remaining(self):
        # функція для виведення поточного стану кавомашини
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money\n")

    def process_input(self, user_input):
        # Основний метод для обробки введення користувача на основі поточного стану
        if self.state == "choosing_action":
            if user_input == "buy":
                self.state = "choosing_coffee"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif user_input == "fill":
                self.state = "filling_water"
                print("Write how many ml of water you want to add:")
            elif user_input == "take":
                self.give_money()
                self.state = "choosing_action"
            elif user_input == "remaining":
                self.show_remaining()
            elif user_input == "exit":
                self.state = "exit"
            else:
                print("Invalid action")

        elif self.state == "choosing_coffee":
            if user_input == "1":
                self.prepare_coffee(250, 0, 16, 4)
            elif user_input == "2":
                self.prepare_coffee(350, 75, 20, 7)
            elif user_input == "3":
                self.prepare_coffee(200, 100, 12, 6)
            elif user_input == "back":
                self.state = "choosing_action"
            else:
                print("Invalid choice")

        elif self.state == "filling_water":
            if not user_input.isdigit():
                print("Invalid input. Please enter a number.")
                print("Write how many ml of water you want to add:")
                return
            self.water += int(user_input)
            self.state = "filling_milk"
            print("Write how many ml of milk you want to add:")

        elif self.state == "filling_milk":
            if not user_input.isdigit():
                print("Invalid input. Please enter a number.")
                print("Write how many ml of milk you want to add:")
                return
            self.milk += int(user_input)
            self.state = "filling_beans"
            print("Write how many grams of coffee beans you want to add:")

        elif self.state == "filling_beans":
            if not user_input.isdigit():
                print("Invalid input. Please enter a number.")
                print("Write how many grams of coffee beans you want to add:")
                return
            self.coffee_beans += int(user_input)
            self.state = "filling_cups"
            print("Write how many disposable coffee cups you want to add:")

        elif self.state == "filling_cups":
            if not user_input.isdigit():
                print("Invalid input. Please enter a number.")
                print("Write how many disposable coffee cups you want to add:")
                return
            self.disposable_cups += int(user_input)
            self.state = "choosing_action"

    def prepare_coffee(self, required_water, required_milk, required_beans, price):
        # Функція для перевірки ресурсів і приготування кави
        if self.water < required_water:
            print("Sorry, not enough water!")
        elif self.milk < required_milk:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < required_beans:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            self.water -= required_water
            self.milk -= required_milk
            self.coffee_beans -= required_beans
            self.disposable_cups -= 1
            self.money += price
            print("I have enough resources, making you a coffee!")

        self.state = "choosing_action"

    def give_money(self):
        # функція для видачі всіх грошей з кавомашини
        print(f"I gave you {self.money}")
        self.money = 0


machine = CoffeeMachine()

while machine.state != "exit":
    if machine.state == "choosing_action":
        action = input("Write action (buy, fill, take, remaining, exit):\n> ")
        machine.process_input(action)
    else:
        user_input = input("> ")
        machine.process_input(user_input)
