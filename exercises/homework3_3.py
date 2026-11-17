shirt = input("What size do you need?( S/M/L/XL):")

if shirt == "S" or shirt == "M":
    color = input("What color do you need?:")
    if color == "violet" or color == "yellow":
        print("Немає в наявності")
    else:
        print("Є в наявності")


elif shirt == "L":
    print("There's no available shirts for this size")


elif shirt == "XL":
    fabric = input("What type of fabric do you need?:")
    if fabric == "бавовна":
        print("Є в наявності")
    else:
        print("Немає в наявності")

else:
    print("Немає в наявності")
