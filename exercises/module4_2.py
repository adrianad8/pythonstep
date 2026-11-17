# Користувач вводить свої ім’я та вік. Якщо введено
# від’ємне число то попросити ще раз ввести правильний вік
# поки не буде введено додатнє число.
# В кінці вивести привітання “Привіт Джон. Тобі 36
# років”


# name = input("What's your name: ")

# while True:
#     age = int(input("Enter your age: "))

#     if age > 0:
#         break
#     print("Not possible, enter your real age: ")

# print(f"Hi {name}! You are {age} years old.")

# Користувач вводить суму грошей, яку він хоче
# відкласти. Далі кожного дня користувач вводить суму, яку
# він кладе в скарбничку.
# Програма зупиняється коли грошей достатньо.
# Виправте помилку в коді


# goal = float(input("Цільова сума? "))

# total = 0

# while True:

#   daily_amount = float(input("Сьогоднішній вклад? "))

#   total += daily_amount

#   if total >= goal:
#     break

# print(f"Мету досягнуто! У скарбничці {total} грн. ")


# Користувач вводить довжину в метрах. Покажіть її у
# ● Ярдах(1 ярд = 0,9144 метра)
# ● Футах(1 фут = 0,3048 метра)
# В кінці спитайте користувача чи продовжувати роботу
# програми.


# yard= 0.9144
# foot = 0.3048


# while True:
#   length = float(input("Enter the length in meters:"))

#   meters_inyards =length / yard
#   meters_infoots = length / foot

#   print(f" In yards is {meters_inyards:.2f}")
#   print(f" In foots is {meters_infoots:.2f}")

#   repeat = input("Continue the program (yes/no)? ")
#   if repeat == "no":
#       break
# print("Finished.")


# У завданні 2 ще виведіть кількість днів за яку була
# зібрана потрібна сума.


goal = float(input("Цільова сума? "))

total = 0
days = 0

while True:
    daily_amount = float(input("Сьогоднішній вклад? "))

    total += daily_amount
    days += 1

    if total >= goal:
        break

print(
    f"Мету досягнуто! У скарбничці {total} грн. зібрана потрібна сума за {days} днів "
)
