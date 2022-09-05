
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
partner1 = name1.lower()
partner2 = name2.lower()
com_name = partner1+partner2
T= com_name.count('t')
R= com_name.count('r')
U= com_name.count('u')
E= com_name.count('e')
total1= (T+R+U+E)
L= com_name.count('l')
O= com_name.count('o')
V= com_name.count('v')
E= com_name.count('e')
total2= (L+O+V+E)
result= str(total1)+ str(total2)
result1 = int(result)
if result1 < 10 or result1 > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result1 >= 40 and result1 <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")