# Користувач вводить число від 1 до 9. Потрібно вивести
# для цього числа таблицю множення.


# while True:

#     number= int(input(" Enter a number from 1 to 9: "))

#     if number > 9 or number < 1:

#         print("Enter a valid number")
#         continue

#     for i in range(1,11):
#      print(number ,"*", i ,"=" ,number * i )


# Користувач вводить свої оцінки поки не введе 0. Після
# чого програма виводить середню оцінку.
# Виправіть помилку в коді


# total = 0
# count = 0

# while True:
#    grade = int(input("Введіть оцінку: "))

#    if grade == 0:

#         break

#    total += grade
#    count += 1

# average_grade = total / count
# print(f"середня оцінка: {average_grade}")


# Напишіть простий калькулятор
# Користувач вводить два числа після чого обирає яку дію
# виконати:
# 1. сума
# 2. різниця
# 3. добуток
# 4. частка
# 5. вихід
# Якщо користувач обрав частку, то переконайтесь що не
# буде ділення на 0. У випадку проблеми виведіть відповідне
# повідомлення.


number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

while True:
    print("1. -Sum")
    print("2. -Substract")
    print("3. -Product")
    print("4. -Quotient")
    print("5. -Exit")

    option = int(input("Chose what to do: "))

    if option == 1:
        print(number1 + number2)

    elif option == 2:
        print(number1 - number2)

    elif option == 3:
        print(number1 * number2)

    elif option == 4:
        if number2 == 0:
            print("Error: you cannot divide by zero. Enter another number")
        else:
            print(number1 // number2)

    elif option == 5:
        break
