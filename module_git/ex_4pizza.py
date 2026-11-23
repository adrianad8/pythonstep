MARGHARITA_PRICE = 150
PEPPERONI_PRICE = 180
FOURCHEESE_PRICE = 200

margharita_quantity = 0
pepperoni_quantity = 0
fourcheese_quantity = 0
total_quantity = 0

margharita_name = "Margharita"
pepperoni_name = "Pepperoni"
fourcheese_name = "Four cheese"


while True:
    print("Menu:")
    print("1- Chose pizza")
    print("2- Exit")
    print("3- Show order")

    option = int(input("Chose what to do: "))

    if option == 1:
        print("1.- Margharita/150 hryvnia")
        print("2.- Pepperoni/180 hryvnia")
        print("3.- Four cheese/200 hryvnia")

        select_pizza = int(input("What pizza do you want: "))

        if select_pizza != 1 and select_pizza != 2 and select_pizza != 3:
            print("Incorrect option")
            continue

        quantity = int(input("How many: "))

        total_quantity += quantity

        if quantity < 0:
            print("Error, it can't be negative.")
            continue
        if total_quantity + quantity > 15:
            print("You can't order more than 15 pizzas")
            continue

        if select_pizza == 1:
            margharita_quantity += quantity
            print(f"You have ordered {quantity} {margharita_name}")
        elif select_pizza == 2:
            pepperoni_quantity += quantity
            print(f"You have ordered {quantity} {pepperoni_name}")
        elif select_pizza == 3:
            fourcheese_quantity += quantity
            print(f"You have ordered {quantity} {fourcheese_name}")

    elif option == 2:
        break

    elif option == 3:
        total_price_marg = 0
        total_price_peppe = 0
        total_price_cheese = 0

        print("Your order:")

        if margharita_quantity > 0:
            total_price_marg = margharita_quantity * MARGHARITA_PRICE
            print(f"Pizza - {margharita_name}")
            print(f"Quantity - {margharita_quantity}")
            print(f"Price - {total_price_marg} hryvnia")

        if pepperoni_quantity > 0:
            total_price_peppe = pepperoni_quantity * PEPPERONI_PRICE
            print(f"Pizza - {pepperoni_name}")
            print(f"Quantity - {pepperoni_quantity}")
            print(f"Price - {total_price_peppe} hryvnia")

        if fourcheese_quantity > 0:
            total_price_cheese = fourcheese_quantity * FOURCHEESE_PRICE
            print(f"Pizza - {fourcheese_name}")
            print(f"Quantity - {fourcheese_quantity}")
            print(f"Price - {total_price_cheese} hryvnia")

        total_cost = total_price_marg + total_price_peppe + total_price_cheese

        print(f"Your total price is {total_cost} hryvnia")
        print("Thanks for ordering here!")
