# Користувач вводить рядок та символ. Порахуйте скільки
# разів цей символ зустрічається у рядку.
# Зробіть двома способами:
# ● з методом count
# ● з циклом for
# Приклад:
# В “it is amazing” символ “і” зустрічається 3 рази

# 1 way
# text = (input("Say something: "))
# symbol = (input("What symbol do you want to count: "))


# number_symbol = text.count(symbol)
# print(f"В {text} символ {symbol} зустрічається {number_symbol} рази")


# 2 way

# text = input("Say something: ")
# symbol = input("What symbol do you want to count: ")

# count = 0

# for letter in text:
#     if letter == symbol:
#         count += 1

# print(f"В {text} символ {symbol} зустрічається {count} рази")


# Користувач вводить рядок. Виведіть наступну
# інформацію:
# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh


# text = input("Enter a phrase: ")
# word = ("python")

# print(len(text))

# if word in text:
#     print("yes")

# else:
#     print("no")


# letter_count = text.count("s") + text.count("z") + text.count("h")
# print(letter_count)


# Користувач вводить тест. Потрібно замінити всі пробіли
# на дефіси. Виправіть помилку в коді


# text = input("Введіть текст: ")

# result = text.replace(" ", "-")
# print(f"Змінений текст: {result}")


# Користувач вводить рядок та слово. Порахуйте скільки
# разів це слово зустрічається у рядку.


# phrase = input("Enter a phrase: ")

# word = input("Write a word: ")


# count = phrase.count(word)

# print(count)


# При оформлені посилки заборонено перевозити
# наступні речі:
# ● ножі
# ● гроші
# ● сильні отрути
# Виправіть помилку в коді

# items = input("Введіть ваші речі: ")
# items = items.lower()

# if "ніж" in items or "гроші" in items or "отрута" in items:
#     print("У вас є речі які заборонено перевозити")
# else:
#     print("Оформлено доставку")


# Користувач вводить текст. Порахуйте скільки в ньому
# літер та цифр.


text = input("Enter something: ")
count = 0
count1 = 0
for ch in text:
    if ch.isdigit():
        count += 1

    if ch.isalpha():
        count1 += 1

print(f"There is {count} numbers and {count1} letters")


# Користувач вводить пароль поки не введе його
# правильно.
# Правильний пароль повинен:
# ● Бути довшим за 8 символів
# ● Містити хоча б одну цифру
# ● Містити хоча б одну літеру


password = "Enter the password: "
