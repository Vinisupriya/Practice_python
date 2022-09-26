# Python program to demonstrate list
# comprehension in Python
  
# below list contains square of all
# odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

# importing "array" for array operations
import array
 
# initializing array with array values
# initializes array with signed integers
arr= array.array('i',[1, 2, 3, 1, 5])
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,5):
    print (arr[i],end=" ")
 
print ("\r")