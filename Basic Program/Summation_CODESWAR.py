def summation(num):
    sum = 0
    for n in range(0, num + 1):
        sum += n
    return sum
num=8
sum1= summation(num)
print(sum1)