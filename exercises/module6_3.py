# Створіть список чисел [1, 8, -5, 9]
# ● Виведіть на екран елементи цього списку
# ● Збільшіть кожне число в 3 рази та виведіть результат
# ● Замініть усі числа більші 10 на 0 та виведіть
# результат


numbers = [1, 8, -5, 9]

print(numbers)

for number in range(len(numbers)):
    numbers[number] = numbers[number] * 3

print(numbers)

for number in range(len(numbers)):
    if number > 10:
        numbers[number] = 0

print(numbers)


# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len

numbers = []

while True:
    number = int(input("Enter a number: "))
    if number == -1:
        break

    else:
        numbers.append(number)

print(numbers)
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers) / len(numbers))


# Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.
# Виправіть помилку в коді

positive = []
negative = []

while True:
    number = int(input("Введіть число (0 для завершення): "))

    if number > 0:
        positive.append(number)
    elif number == 0:
        break
    else:
        negative.append(number)

print("Додатні числа:", positive)
print("Від'ємні числа:", negative)


# Користувач вводить зарплати співробітників, поки не
# введе -1. Після чого вводить відсоток на який треба
# збільшити усім зарплату.
# Виведіть нові зарплати


salaries = []

while True:
    salary = int(input("Enter the salary of the workers: "))
    if salary == -1:
        break
    else:
        salaries.append(salary)


percent = int(input("How much percent do you give a raise: "))
for salary in salaries:
    new_salary = salary * (1 + percent / 100)

    print(new_salary)
