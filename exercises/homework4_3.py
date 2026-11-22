# Напишіть програму для роботи онлайн магазину.
# Товари:
# ● подушка – 650 грн
# ● ковдра – 1700 грн
# ● лампа – 500 грн
# ● брелок – 60 грн
# Меню дій:
# ● додати товар
# ● видалити товар
# ● очистити кошик
# ● показати вміст кошики та суму покупки
# ● вихід
# Користувачу показується меню один раз на початку
# програми
# Користувач вибирає номер дії після чого за потреби
# вводить назву товару то його кількість
# У випадку неправильно введених даних повідомити про
# це та повернутись до вибору номера дії
# Створіть для кожного товару змінну з кількістю цього
# товару у кошику для подальшої роботи


pillow_quantity = 0
blanket_quantity = 0
lamp_quantity = 0
keychain_quantity = 0

while True:
    print("Menu:")
    print("1- Add product")
    print("2- Delete product")
    print("3- Clear basket")
    print("4- Show basket and price")
    print("5- Exit")

    selection = input("Select what you want to do: ")

    if selection == "1":
        print("Products:")
        print("pillow")
        print("blanket")
        print("lamp")
        print("keychain")

        chose_product = input("Select what product do you want: ")

        quantity = int(input("How many do you want to delete(numbers): "))

        if chose_product == "pillow":
            pillow_quantity += quantity

        elif chose_product == "blanket":
            blanket_quantity += quantity

        elif chose_product == "lamp":
            lamp_quantity += quantity

        elif chose_product == "keychain":
            keychain_quantity += quantity

        else:
            print("This product is incorrect")

    elif selection == "2":
        print(f"You have {pillow_quantity} pillows.")
        print(f"You have {blanket_quantity} blankets.")
        print(f"You have {lamp_quantity} lamps.")
        print(f"You have {keychain_quantity} keychains.")

        chose_product = input("Select what product do you want to delete: ")

        quantity = int(input("How many do you want(numbers): "))

        if chose_product == "pillow":
            if quantity <= pillow_quantity:
                pillow_quantity -= quantity
            else:
                print("Error, there are not enough products")

        elif chose_product == "blanket":
            if quantity <= blanket_quantity:
                blanket_quantity -= quantity
            else:
                print("Error, there are not enough products")

        elif chose_product == "lamp":
            if quantity <= lamp_quantity:
                lamp_quantity -= quantity
            else:
                print("Error, there are not enough products")

        elif chose_product == "keychain":
            if quantity <= keychain_quantity:
                keychain_quantity -= quantity
            else:
                print("Error, there are not enough products")

    elif selection == "3":
        pillow_quantity = 0
        blanket_quantity = 0
        lamp_quantity = 0
        keychain_quantity = 0

        print(f"You have {pillow_quantity} pillows.")
        print(f"You have {blanket_quantity} blankets.")
        print(f"You have {lamp_quantity} lamps.")
        print(f"You have {keychain_quantity} keychains.")

    elif selection == "4":
        print(f"You have {pillow_quantity} pillows.")
        print(f"You have {blanket_quantity} blankets.")
        print(f"You have {lamp_quantity} lamps.")
        print(f"You have {keychain_quantity} keychains.")

        pillow_price = pillow_quantity * 650
        blanket_price = blanket_quantity * 1700
        lamp_price = lamp_quantity * 500
        keychain_price = keychain_quantity * 60

        total_price = pillow_price + blanket_price + lamp_price + keychain_price

        print(f"Your total price is {total_price} hrivnia.")

    elif selection == "5":
        break

    else:
        print("There is no such an option")
        continue
