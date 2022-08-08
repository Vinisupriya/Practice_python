'''str=  input("Enter your string")
print(str) 
for i in range (0, len(str)) :
    print(str ) '''

n = input("Enter the word and see if it is palindrome: ") #check palindrome
if n == n[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")
 