bot_name = "AntBot"
birth_year = 2024

print(f"Hello! My name is {bot_name}.")      # зривітання від бота
print(f"I was created in {birth_year}.")

print("Please, remind me your name.")        # запит імені користувача
your_name = input()

print(f"What a great name you have, {your_name}!")        # відповідь бота

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input("Remainder when your age is divided by 3: "))
remainder5 = int(input("Remainder when your age is divided by 5: "))
remainder7 = int(input("Remainder when your age is divided by 7: "))

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105           # збчислення віку

print(f"Your age is {age}; that's a good time to start programming!")         # зиведення результату

print("Now I will prove to you that I can count to any number you want.")   # запитуємо число
tik = int(input("Enter a positive number: "))

for i in range(tik + 1):             # підрахунок від 0 до введеного числа
    print(f"{i} !")

# Завершення програми
print("Completed, have a nice day!")       # виведення завершення
