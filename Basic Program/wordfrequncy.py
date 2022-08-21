# Find duplicat words and frequency count
# without using sort function
sentence = 'Hi vini vini and suvetha Are are worst friends'
str= sentence.lower().split()
#str=sentence.split( )
print ( str)
str2=[]  #empty string to store Non-duplicate value

for i in str:
    if i not in str2:
        str2.append(i) # add non-duplicate values in str2
print (str2)
for i in range ( 0, len(str2)):
    if (str.count(str2[i]) >1):
        print ('frequency of', str2[i], 'is :', str.count(str2[i]))
    # counting number of words in str(original string) to str2( non duplicate value)



