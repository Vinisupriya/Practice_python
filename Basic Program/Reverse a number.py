number = int(input("Enter your number"))
rev=0
while(number>0):
    rev=(rev*10)+number%10
    number=number//10
print("The reverse number is",rev)
