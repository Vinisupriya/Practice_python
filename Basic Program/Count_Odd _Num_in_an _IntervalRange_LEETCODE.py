#Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
#Example 1:
#Input: low = 3, high = 7
#Output: 3
#Explanation: The odd numbers between 3 and 7 are [3,5,7].
#CODE
low =1
high=10
k=0
for i in range(low,high+1):
    if i%2 == 0:
        continue
    else:
        k= +i
        print( "The odd numbers between" + str(low) + "and "+ str(high)+" are", k)


