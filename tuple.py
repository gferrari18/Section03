
list = []
tuple = ()
items = ""


while items != "none":
    items = input("enter a grocery item, or none to exit: ")
    if items != "none":
        list.append(items)

print("Now go to the store! this is your item list: ")
for x in list:
    print(x)


while len(list) != 0:
    cart = input("what did you put in your cart?")
    if cart in list:
        for things in tuple:
            (cart, price, quantity) = things
        price = int(input("what was the price of the item? "))
        quantity = input("How many did you get? ")
        list.remove(cart)
    elif cart not in list:
        print("Item not in list. Enter an item that was previously added to the list")

print(tuple)
print("Go check out!")

