 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size == "S": 
    price = 15
if size == "M":
    price =20
if size == "L":
    price = 25
if add_pepperoni == "Y":
    if size == "S":
         price+= 2
    else:
         price+=3
else:
    price+= 0
if extra_cheese == "Y":
    bill = price+ 1
    print(f"Your final bill is: ${bill}." )
else:
    bill = price
    print(f"Your final bill is: ${bill}." )