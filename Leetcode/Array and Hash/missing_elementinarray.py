

arr =[1, 2, 4, 6, 3, 7, 8]
n = len(arr)

def missingElements(arr,n):
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(arr)
    return total - sum_of_A         
        
result = missingElements(arr,n)
print(result)
