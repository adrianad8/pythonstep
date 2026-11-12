# Користувач вводить час у хвилинах, виведіть скільки це 
# секунд. 
# Якщо введено від’ємне число виведіть 
# повідомлення “Час має бути додатнім” 

# time_min = int(input("Enter the time in minutes: "))

# time_sec = time_min* 60
# if time_min > 0 :
#     print (f"{time_sec} seconds")

# else: 
#     print("Час має бути додатнім")



# # Напишіть програму для перевірки правильності паролю. 
# # Якщо користувач ввів правильний пароль то виведіть 
# # “Доступ дозволено” інакше “Доступ заблоковано” 
# # Правильний пароль secret_password = "OpenSesame123"



# password = str(input("Enter your password: "))

# secret_password = "OpenSesame123"

# if password == secret_password : 
#     print("Доступ дозволено")

# else:
#     print("Доступ заблоковано")





# # Користувач вводить довжину в метрах та в що їх 
# # перевести(сантиметри(см) чи кілометри(км)) 
# # Напишіть програму яка переводить метри в бажану 
# # одиницю вимірювання. Якщо користувач ввів не см  чи км 
# # то повідомте про помилку 



# length_meter = float(input("Enter your length in meters: "))
# convert = str(input("Convert to (cm/km):  "))

# length_cm = length_meter * 100
# length_km = length_meter / 1000

# if convert == "cm":
#     print(length_cm)
# elif convert == "km": 
#     print (length_km)

# else: 
#     print ("Error! Enter the length only in km or cm")


# # Прочитайте уривок нижче наведеного твору 
# # — Гаразд, — сказав комп’ютер і знову поринув у мовчання. 
# # Двоє чоловіків нервово вовтузилися. Напруження було 
# # нестерпним.


# answer = input("Відповідь на Велике Питання Життя, Всесвіту і Всього Іншого: ") # asks the person 

# if answer == "сорок-два": # tells that if they say this it will be correct
#     print("Правильно") 

# if answer == "42": # if they say 42 it returns that it's correct
#    print("Правильно")

# elif answer == "сорок два": # if they say this answer it returns that it's correct
#    print("Правильно")

# else:  # if they write something else than these 3 answers it returns that it'ss not correct
#    print("Не правильно")



# Потрібно написати програму яка переводить оцінки в 
# шкалу незадовільно відміно

# grade = int(input("Введіть оцінку: ")) 
 
# if grade == 2: 
#    print("Незадовільно") 
# elif grade == 3: 
#    print("Задовільно") 
# elif grade == 4: 
#    print("Добре") 
# elif grade == 5: 
#    print("Відмінно") 
# else: 
#    print("Оцінка має бути від 2 до 5")


# Ви плануєте замовити піцу для компанії людей. 
# Користувач вводить ціну однієї піци, кількість піц та 
# ваш загальний бюджет. 
# Перевірте чи вистачає вам грошей. Якщо ні то виведіть 
# скільки саме не вистачає

price_one = int(input("Price per one pizza: "))
amount_pizza= int(input("How many pizzas: "))
budget = float(input("What's your budget: "))


total = price_one * amount_pizza 

if total > budget: 
   print ( "There isn't enough money")
   print(f"It lacks {total-budget} ")


