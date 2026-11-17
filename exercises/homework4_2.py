# Користувач вводить оцінку за іспит(від 1 до 5) поки не
# введе правильне число. Після цього виведіть цю оцінку
# текстом
# 1. Дуже погано
# 2. Погано
# 3. Задовільно
# 4. Добре
# 5. Чудово


# while True:
#     grade =int(input("Enter your grade: "))

#     if grade == 1:
#         print("Дуже погано")
#         break

#     elif grade == 2:
#         print("Погано")
#         break

#     elif grade == 3:
#         print("Задовільно")
#         break

#     elif grade == 4:
#         print("Добре")
#         break

#     elif grade == 5:
#         print("Чудово")
#         break

#     elif grade > 5 or grade < 1:
#         print("Incorrect. Enter the real number")


# Проводиться опитування « Чи потрібно будувати більше
# дитячих садків у вашому місті?»

# Напишіть програму для підрахунку відповідей.
# Користувач вводить слова «так» або «ні» поки не введе
# слово «стоп», після чого треба показати кількості «так» та
# «ні» і також яких голосів більше.

# Якщо введено невідоме слово, то вивести повідомлення
# про помилку та продовжити підрахунок

# vote_yes = 0
# vote_no = 0

# while True:
#     vote = input("Чи потрібно будувати більше дитячих садків у вашому місті? (так/ні): ")
#     if vote == "так":
#         vote_yes += 1

#     elif vote == "ні":
#         vote_no += 1

#     elif vote == "стоп":
#         break

#     else:
#         print("Error")


# print(f"There are {vote_yes} positives votes")
# print(f"There are {vote_no} negatives votes")

# if vote_yes > vote_no:
#     print("There are more positives votes than negatives")

# elif vote_yes < vote_no:
#     print("There are more negative votes than positive")

# else:
#     print("It's a tie")


# Нижче наведено код який зупиняється коли користувач
# вводить число 0, але він не працює.
# Виправіть помилку

print("Введіть число (0 для виходу):")

while True:
    num = input("Ваше число: ")

    if num == "0":
        print("Вихід з програми.")
        break

    print(f"Ви ввели: {num}")
