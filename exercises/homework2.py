# Користувач вводить 2 числа, потрібно вивести середнє
# арифметичне.  Але програма не працює


num1 = int(input("перше число: "))
num2 = int(input("друге число: "))

sum = num1 + num2
average = sum / 2

print("Сума:", sum)
print("Середнє:", average)

# Користувач вводить суму в гривнях та курс долара.
# Переведіть гривні в долари та виведіть на екран


uan = float(input("enter your value in hrivnia: "))
kurs = float(input("enter the rate of the dollar: "))

dollar = uan / kurs

print(f"Your value in dollars is: {kurs:.2f}")


# Користувач вводить ціну товару та відсоток знижки.
# Виведіть суму знижки

price = float(input("Enter the price: "))
discount_percent = int(input("What's the percent of the discount: "))

number_discount = price * (discount_percent / 100)

print(f"The discount is {number_discount} ")

# Користувач вводить 3 числа: час повільної/швидкої
# ходьби та бігу.
# Напишіть код який обчислює окремо кількість калорій
# спалених під час цих активностей.
# Також виведіть загальну кількість спалених калорій.


time_slow = int(input("Enter the minutes of slow walk: "))

time_fast = int(input("Enter the minutes of fast walk: "))
time_run = int(input("Enter the minutes of run: "))

cal_slow = time_slow * 3
cal_fast = time_slow * 4.5
cal_run = time_run * 9

total_cal = cal_slow + cal_fast + cal_run

print(
    f"Your burned calories are:\n Slow walk: {cal_slow}\n Fast walk: {cal_fast} \n Run: {cal_run}"
)
print(f"The total burned calories are: {total_cal}")
