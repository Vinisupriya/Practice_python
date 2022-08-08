def reverse(string) :
	reversed_string=""
	for i in string:
		reversed_string = i+ reversed_string #
	print("The reversed string is : " , reversed_string)

string= input("Enter your string : ")
print("The String is", string)
reverse(string)

