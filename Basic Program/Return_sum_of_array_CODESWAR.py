#You get an array of numbers, return the sum of all of the positives ones.

#Example [1,-4,7,12] => 1 + 7 + 12 = 20

#Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    sum=0
    for i in range(0, len(arr)):
        if arr[i]>0:
            sum = sum + arr[i]
        else:
            continue
            return 0
    return sum
            
arr= [-10,-10,-20,-10]
arr1= positive_sum(arr)
print("Sum of all the elements of an array: " + str(arr1))
