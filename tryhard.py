from sys import call_tracing




list = []
cart = []
item = ""
total = 0

while item != "none":
    item = input("enter item name: ")
    if item != "none":
        list.append(item)

print("Nice, go to the store!")

while len(list) != 0:
    item = input("Enter item name: ")
    if item in list:
        list.remove(item)
        price = float(input("enter item price: "))
        qty = int(input("enter price qty: "))
        evr = (item, price, qty)
        cart.append(evr)
    elif item not in list:
        print("You must enter an item that was previously added to the list!")

for x in cart:
    (item,price,qty) = x
    print("Item name: " + item + " Price: " + str(price) + " Qty: " + str(qty))
    total = total + (float(price) * int(qty))
print("Total = " + str(total))















"""

tp1 = []
tp2 = []
tp3 = []

fn = ()

item = ""
price = int("")
quant = int("")

while item != "none":
    item = input("Enter item: ")
    price = input("Enter price: ")
    quant = input("Enter quantity: ")
    if item != "none":
        tp1.append(item)
        tp2.append(price)
        tp3.append(quant)

for 

"""