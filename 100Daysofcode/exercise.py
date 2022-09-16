# 1 BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
ht= float(height)
wt= int(weight)
bmi = (wt) / (ht**2)
print(int(bmi))

# 2 Adds the digits in a 2 digit number. 
#new problem
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")
#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
#Add the two digits togeter
two_digit_number = first_digit + second_digit
print(two_digit_number)
# Another method
num= int(two_digit_number)
rem= num // 10
quo = num % 10
add= rem + quo
print(add)

# 3 Life in weeks
#Create a program using maths 
# using f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old

age = input("What is your current age?")
rem = 90-int(age)
month = rem * 12
days = rem * 365
weeks = rem* 52
print(f"you have {days} days, {weeks}weeks, and {month} months left")






