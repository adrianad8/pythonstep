print("Menu:")
print("1- Chose pizza")
print("2- Exit")

option = int(input("Chose what to do: "))
while True:
    if option == 1:
        select_pizza = input("What pizza do you want: ")
        quantity = int(input("How many: "))

        print(f"You have ordered {quantity} {select_pizza}")
