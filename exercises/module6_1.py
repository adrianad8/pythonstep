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

text = input("Say something: ")
symbol = input("What symbol do you want to count: ")

count = 0

for letter in text:
    if letter == symbol:
        count += 1

print(f"В {text} символ {symbol} зустрічається {count} рази")
