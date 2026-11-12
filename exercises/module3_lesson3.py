# Каса кінотеатру розраховує вартість квитка в залежності 
# від віку користувача: 


# age= int(input("How old are you: "))


# if age < 12:
#     price =80
# if age >= 12 and age <= 65:
#     price= 200

# if age > 65:
#     price= 120


# print (f"Your price is {price} euros")
# print("Have a great day!")



# Користувач вводить назву місяця та число. Потрібно 
# вивести яке сьогодні свято. 
# Якщо сьогодні звичайний день то так і сказати 
# користувачу. 


# day = int(input("Enter a day: "))
# month = (input("Enter a month: "))



# if day == 1 and month == "january" :
#    print ("Today is New Year!") 

# elif day == 14 and month == "february" :
#    print ("Today is St Valentine's day!") 

# elif day == 25 and month == "december" :
#    print ("Today is Christmas!")

# elif day == 1 and month == "april" :
#    print ("Today is Laugh's day!")


# else: 
#     print("Today's a normal day!")




#     У завданні 1 треба купити білети трьом людям. 
# Змініть код таким чином щоб можна було ввести три 
# числа(вік трьох людей) та вивести скільки коштує білет 
# для кожної людини окремо. 
# Також вивести загальну суму.




# age1= int(input("How old is the first person: "))
# age2= int(input("How old is the second one: "))
# age3= int(input("How old is the third one: "))


# if age1 < 12:
#     price1 =80
# elif age1 >= 12 and age1 <= 65:
#     price1= 200

# elif age1 > 65:
#     price1= 120



# if age2< 12:
#     price2 =80
# elif age2 >= 12 and age2 <= 65:
#     price2= 200

# elif age2 > 65:
#     price2= 120



# if age3 < 12:
#     price3 =80
# elif age3 >= 12 and age3 <= 65:
#     price3= 200

# elif age3 > 65:
#     price3= 120


# total= price1+ price2 + price3

# print (f"The price of the first person is {price1}, of the second one: {price2}, the third one: {price3}.")
# print(f"Your total price is {total}")
# print("Have a great day!")



# Користувач вводить назву товару, програма повинна 
# перевірити чи можна продати цей товар 
# Якщо хочуть купити алкоголь або тютюн то спитайте 
# вік. Продаж дозволено з 18 років 
# Якщо це ліки то попросіть рецепт від лікаря.(ди


product = input("Введіть назву товару: ") 


if product == "алкоголь" or product == "тютюн": 
    age = int(input("Введіть ваш вік: ")) 
    if age >= 18: 
        print("Дозволено до продажу") 
    else: 
        print("Заборонено до продажу") 
 
 
elif product == "ліки": 
    prescription = input(" У вас є рецепт від лікаря?") 
 
    if prescription == "так": 
        print("Дозволено до продажу") 

    else: 
            print("Заборонено до продажу")
 
# 

else: 
   print("Дозволено до продажу") 





# Для того щоб оформити замовлення в онлайн 
# магазині потрібно зайти на сайт, добавити товар в кошик 
# та оплатити замовлення. 
# Нижче наведено код цієї програми








