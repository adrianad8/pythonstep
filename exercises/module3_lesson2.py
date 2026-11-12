
# Користувач вводить свій вік, якщо він працездатного 
# віку(18-65) то виведіть фразу «Працездатний/на», інакше 
# «Непрацездатний/на»

# age = int(input("Enter your age: "))

# if age >= 18 and age <=65 :
#     print("Працездатний/на")

# else:
#     print("Непрацездатний/на")

# # До завдання 2 з попереднього заняття добавте додаткову 
# # перевірку: щоб отримати доступ користувач повинен ще й 
# # ввести правильний логін secret_login = "AliBaba"


# secret_password = "OpenSesame123"
# secret_login = "AliBaba"

# password = input("Enter your password: ")
# login = input("Enter your login: ")


# if password == secret_password and login ==secret_login :
#     print("Доступ дозволено")
# else:
#     print("Доступ заблоковано")


# # Оформіть чек покупки. Користувач вводить ціну за 
# # одиницю товару, кількість товару та свій вік. 
# # Якщо користувач неповнолітній або старший за 65 
# # років, то застосуйте знижку 15% 

# price = float(input("Enter the price per item: "))
# amount = int(input("How many items do you have: "))
# age = int(input("Enter your age: "))

# total = price * amount

# if age < 18 or age > 65: 
#     discount = total * 0.15
#     new_price = total - discount 

#     print(f"You had a discount of 15%, your total is {new_price}")

# else: 
#     print (f"Your total is {total}")


# # Орендувати авто можна лише якщо 
# # ● у вас є ліцензія 
# # ● ви повнолітні 
# # ● ви не потрапляли в дтп 
# # Оцініть якість написаного коду, спробуйте його 
# # спростити використавши and\or

# age = 23 
# has_license = "так" 
# accidents = 0 
 
# if age >= 18 and has_license == "так" and accidents == 0 : 
#    print("Оренда дозволена") 

# else: 
#     print("Оренда заборонена") 
   

# Напишіть програму яка запитує у користувача ціну 
# покупки та виводить загальну вартість(покупки + доставка) 
# Базова ціна доставки: 120 грн 
# Знижка діє лише на доставку 


# price = int(input("What's the price of the purchase: "))
# shipping_cost = 120 
 
# if price < 500: 
#     total = shipping_cost + price
#     print (f"Your total is {total}")

# elif price >= 500 and price <= 1000: 
#     total = shipping_cost + price * 0.95 
#     print (f"Your total is {total}")

# elif price >= 1000 and price <= 2000: 
#     total = shipping_cost + price * 0.8
#     print (f"Your total is {total}")

# else : 
#     total = price
#     print (f"Your total is {total}")





# Виведіть відсоткову ставку, загальну суму кредиту та  
# щомісячний платіж 


loan = int(input("Enter your loan : "))
duration = int (input("What's the period in years: "))


if loan <= 10000 and duration <= 3 : 
    rate = 8

elif loan <= 10000 and duration >3: 
    rate = 10

elif loan >10000 and loan <= 50000 and duration <=3 :
    rate = 12

elif loan >10000 and loan <= 50000 and duration >3: 
    rate = 14

else: 
    rate= 20

total = loan * (1 + rate/100) ** duration
monthly_pay = total / ( duration* 12) 


print ( f" Your rate is: {rate}  ")
print ( f" Your total credit is: {total:.1f} ")
print ( f"Your monthly payment is: {monthly_pay:.1f} ")