# Read a file

'''file = open("vini.txt" ,"r" )
print(file.read())'''

# Write a file With TRY AND EXPECT

try:
    file = open("vini.txt" ,"w" )
file.write("Hello world")
file.close()

file= open("vini.txt","r")
for line in file:
    print(line)

except FileNotFoundError:
    print("Error")
else:
    file.close()
