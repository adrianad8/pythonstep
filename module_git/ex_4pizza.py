print("Menu:")
print("1- Chose pizza")
print("2- Exit")

option = int(input("Chose what to do: "))
while True:
    if option == 1:
        print("Margharita - 150 hryvnia")
        print("Pepperoni - 180 hryvnia")
        print("Four cheese - 200 hryvnia")

        select_pizza = input("What pizza do you want: ")
        quantity = int(input("How many: "))

        if select_pizza == "Margharita":
            price = 150
        if select_pizza == "Pepperoni":
            price = 180
        if select_pizza == "Four cheese":
            price = 200
        else:
            print("Incorrect name")

    print(f"You have ordered {quantity} {select_pizza}")

    if option == 2:
        break
