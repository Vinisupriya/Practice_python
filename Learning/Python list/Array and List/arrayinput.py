# How to get input from user in Array

n= int(input("Enter your length of the array"))
arr = []
for i in range( n-1):
    m = int(input("Enter the element"))
    arr.append(m)
print(arr)

# Add elements in array

sum=0
for i in arr:
    sum = sum + i
print(sum)

# summation of natural number
total = int( n * (n+1)/2)
print(total)
#To find missing number in array
result = total - sum
print(f"The missing value is {result}")



