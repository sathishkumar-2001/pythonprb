#tc 0(n) sc 0(1)
def productofmax(arr):
    max1,max2 = arr[0],float("-inf")
    min1,min2 = arr[0],float("inf")
    n = len(arr)
    for i in range(1,n):
        if arr[i]>max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i]>max2:
            max2 = arr[i]
        if arr[i]<min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i]<min2:
            min2 = arr[i]
    return max(max1*max2,min1*min2)
    

print(productofmax([4,6,-4,1,2]))