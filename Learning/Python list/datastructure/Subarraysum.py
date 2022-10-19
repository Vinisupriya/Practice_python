
# Sumof2array
#method 1
nums= [2,1,3,4,7]
target = 9
def twoSums(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]== target:
                return [i,j]
                 
result = twoSums(nums)
print(result)
