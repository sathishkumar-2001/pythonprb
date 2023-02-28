#tc o(nlogn) sp o(1)
def countpairs(num,target):
    num.sort()
    n = len(num)
    left = 0
    right = n-1
    count = 0
    while (left < right):
        current_sum = num[left] + num[right]
        if current_sum == target:
            count+=1
            left+=1
            right+=1
        elif current_sum>target:
            right-=1
        else:
            left+=1

    return count

num = [1,5,-1,7,100]
print(countpairs(num, 6))