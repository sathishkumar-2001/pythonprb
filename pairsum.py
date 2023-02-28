#time complexity o(n) space complexity o(n)
def countpairs(num,target):
    set_numbers = set()
    n = len(num)
    count = 0
    for i in range(n):
        required = target - num[i]
        if required in set_numbers:
            count+=1
        set_numbers.add(num[i])
    return count

num = [1,5,-1,7,100]
print(countpairs(num, 6))
