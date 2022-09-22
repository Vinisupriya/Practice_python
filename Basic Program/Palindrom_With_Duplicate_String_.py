str= 'Hi Vini Vini and Suvetha Are are  both Bothu worst friends Madam Madam'
str1= str.lower().split()
print (str1)
str2=[]
for i in str1:
        if i not in str2:
            str2.append(i)
print(str2)
for i in range (0 ,len(str2)):
    if(str1.count(str2[i])>1):
        print("Frequency of",str2[i],'is', str1.count(str2[i]))
        str3=""
        for j in str2[i]:
            str3= j+str3
        print(str3)
        if(str3 == str2[i]):
            print(str2[i],'is palindrom')
        else:
            print(str2[i],'is  not a palindrom')

