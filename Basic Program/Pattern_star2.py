# Star pattern 2
num= int(input("Enter your range"))
for i in range(num-1):
    print("  ", end=" ")
    for j in range(i+1):
        print("*", end=" ")

    print("\r")
