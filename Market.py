

list = []

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
        list.remove(cart)
    
print("Go check out!")

