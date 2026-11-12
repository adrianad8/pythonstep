#task 1 
#Користувач вводить радіус кола. Потрібно обрахувати 
# площу круга та вивести результат з двома знаками після 
# коми. 
# Розтавте команди нижче у правильному порядку та 
# додайте підписи з описом що робить команда(є 
# продовження на наступній сторінці) 


# # this creates a variable of the radius so that the person can put the length 
# radius = float(input("Введіть радіус: "))

# # # its the variable of pi
# pi = 3.1415

# # # calculates the area
# area = pi * radius ** 2

# # # tells to print the area of the circle with two decimals
# print(f"Площа кола: {area:.2f}") 
 



# # #task 2 
# # Користувач вводить ціну однієї кружки та загальний 
# # бюджет. Виведіть скільки кружок можна купити

# price= float(input("Введіть ціну однієї кружки: ")) 
# total_money = float(input("Введіть бюджет: ")) 

# cups= total_money //price

# print (f"Можна купити: {cups:.0f} кружки ")



#task 3 
# Користувач вводить довжину в метрах. Виведіть цю 
# довжину в футах та ярдах.

# length = float(input("Enter your length in meters: ")) 
# foot = 3.2808399
# yard = 1.0936133

# meters_foot= length*foot
# meters_yard= length*yard
# print( f"Your length in:\nfoot: {foot1}\nyard: {yard2}")


# #task 4 
# #У завданні 2 виведіть ще залишок коштів 

# price= float(input("Введіть ціну однієї кружки: ")) 
# total_money = float(input("Введіть бюджет: ")) 

# cups= total_money //price
# rest= total_money%price 
# print (f"Можна купити: {cups:.0f} кружки ")
# print(f"Your change would be {rest}")

#task 5 
#Користувач вводить загальну кількість хвилин. 
#Переведіть їх у години та хвилини. 

# total_min = int(input("Введіть кількість хвилин: "))
# hours= total_min //60
# minutes= total_min % 60 
# print(f"{total_min} is {hours} hours and {minutes} minutes")


#tasks 6
# Щоб спекти пиріг потрібно 4 яблука та 1.2 літра молока. 
# Користувач вводить кількість яблук та молока(у літрах). 
# Виведіть скільки він може спекти пирогів. 
# Виведіть скільки яблук та молока залишиться.

amount_apples= int(input("Введіть кількість яблук: "))
amount_milk= float(input("Введіть кількість молока (л): "))

pies_apples= amount_apples//4
pies_milk= amount_milk//1.2

pies = (min(pies_apples, pies_milk))

resta_apples= amount_apples - (pies*4)
resta_milk =  amount_milk - (pies*1.2)


print(f"Можна спекти пирогів: {pies} \n Залишиться яблук: {resta_apples} \n Залишиться молока: {resta_milk}" )


#task 7
# Користувач вводить суму вкладу в банк та відсоток 
# ставки.  
# ● Обчисліть скільки користувач отримує через 5 років, 
# якщо кожного року сума вкладу збільшується на даний 
# відсоток 
# ● Виведіть суму вкладу кожного року окремо


#task 8
# ористувач вводить кількість днів. Виведіть скільки це 
# років, тижнів та днів. 
total_days = int(input("Введіть кількість днів: "))

year= total_days//365
year_resta= total_days % 365

weeks=year_resta // 7

days= year_resta %7


Введіть кількість днів: 398 
398 днів — це 1 рік, 4 тижні та 5 днів.