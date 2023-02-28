#tc o(n) and sc o(n)
def subarray(num):
    num_set = set()
    n = len(num)
    prefixarray = [0] * n
    for i in range(n):
        if i == 0:
            prefixarray[i] = num[i]
        else:
            prefixarray[i] = num[i] + prefixarray[i-1]

    for i in range(n):
        if prefixarray[i] in num_set:
            return True
        num_set.add(prefixarray[i])
    if 0 in num_set:
        return True
    else:
        return False







num = [4,2,-3,1,7]
print(subarray(num))