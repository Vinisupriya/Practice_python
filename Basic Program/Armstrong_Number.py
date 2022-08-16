# without using power function
num = 153  # or n=int(input()) -> taking input from user
s = num  # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = num % 10
    sum1 = sum1+(r**b)
    num = num//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")
 