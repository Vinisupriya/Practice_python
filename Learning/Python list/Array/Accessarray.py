#Create Array
import array as arr
a = arr.array("i",[12,15,16])
print(a)

#Accessing Array
print(a[2])

#Basic array operation
#1) Finding len of the array
len(a)

#Adding and changing element in array
# append() extend() insert()
b = arr.array("i",[12,15,16])
b.append(25)
c= arr.array("i",[12,15,16])
c.extend([2,4,5,6])
d= arr.array("i",[12,15,16])
d.insert(2,5,6)
#Removing element
# pop() and remove()
a.pop(2)
a.remove(5)

#Array concat
f =arr.array('d') # creating empty array
f=a+b

#slicing
a[0:3] #print 0 to 2 
# loop

for x in a:
    print(x)