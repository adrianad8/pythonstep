# Користувач вводить рядок та індекс. Виведіть символ
# під цим індексом. Якщо індекс завеликий, виведіть
# інформацію про помилку.


# word = input("Enter a phrase: ")
# index = int(input("Enter an index: "))

# if index >= len(word) or index < 0:
#     print("Error. The index is not in the range.")

# else:
#     print(word[index])

# Користувач вводить рядок та два індекси. Виведіть
# зріз рядка. Виправіть помилку в коді

# text = input("Введіть рядок: ")

# start = int(input("Введіть початковий індекс: "))
# end = int(input("Введіть кінцевий індекс: "))

# segment = text[start:end]

# print(segment)

# Користувач вводить рядок та число n. Виведіть перші
# n символів. Також виведіть останні n символів.

# line = input("Enter a line: ")
# n = int(input("Enter a number: "))


# first = line[:n]

# last = line[-n:]

# print(first)
# print(last)


# Користувач вводить рядок. Перевірте чи це
# речення(закінчується на .!?)


# line = input("Enter a phrase: ")

# if line[-1] == "." or line[-1] == "!" or line[-1] == "?":
#     print("This is a phrase that ends with !?.")

# else:
#     print("This phrase doesn't end in .!?")


# Користувач вводить рядок. Перевірте чи перший
# символ – це велика літера. Виправіть помилку в коді


# text = input("Введіть рядок: ").lower()

# if text[0].isupper():
#     print("Перший символ — велика літера")
# else:
#     print("Перший символ — не велика літера")


# Користувач вводить рядок. Перевірте чи це
# паліндром(читається задом наперед так само).
# Приклади: Кіт утік, око, потоп


# text = input("Enter something: ")

# if text == text[::-1]:
#     print("It's a palindrom")

# else:
#     print("Not a palindrom")


# Користувач вводить рядок та символ. Виведіть індекс
# цього символу.


# line = input("Enter a phrase: ")

# symbol = input("Enter a symbol: ")

# index = line.find(symbol)

# print(index)


# Користувач вводить рядок та символ. Виведіть усі
# індекси цього символу, якщо він зустрічається декілька
# разів.


line = input("Enter a phrase: ")
symbol = input("Enter a symbol: ")
