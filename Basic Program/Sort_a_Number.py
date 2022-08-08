number = [33,12,2,67,2]

for i in range(len(number)):
    for j in range ( i+1 , len(number)):
        if number[i] >= number[j] :
            #number[i] ,number[j] = number[j],number[i]
            temp = number [i]
            number[i] = number[j]
            number[j]= temp
print (number)
