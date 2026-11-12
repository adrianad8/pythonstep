# Користувач вводить ціну за одиницю товару та кількість 
# товару. Якщо загальна сума більша за 500грн або купівля 
# оптом(більше 10 шт), застосувати знижку 10% 

price= float(input("How much costs one item:"))
amount= int(input("How many items:"))
if price > 500 or amount > 10:
    price = price * 0.9

total = price * amount 
print (f"Your total is {total}.")











# Користувач вводить назву дня тижня потрібно визначити 
# чи це вихідний. 
# Виправте помилку в коді 
# Як закінчите попросіть виправити помилку Student 
# Helper та порівняйте ваші відповіді

day = input("Введіть день тижня:") 
 
if day == "субота" or day== "неділя": 
   print("Вихідний") 

else:
    print("Робочий день")






# Напишіть програму яка імітує цю розмову за правилом

dialog = input("Say something:")

if dialog == "9": 
    print("10")

elif dialog == "10" or dialog == "да":
    print("да")

elif dialog == (""):
    print("10!!!")

else:
    print ("Ой не чує баба глуха як тетеря")

# ористувач вводить ширину та висоту прямокутника. 
# Програма повинна вивести площу та периметр 
# Зробіть цю задачу за допомогою ШІ Інтерн 
# Покроково поясніть йому що потрібно робити 
# Додайте посилання на ваш чат спілкування з ШІ



height = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = height * width
perimeter = 2 * (height + width)

print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)