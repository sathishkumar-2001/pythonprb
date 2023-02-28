#tc o(n) sc o(n)
def maxlensubarr(arr,tar):
    n = len(arr)
    prefixsub = [0] * n
    for i in range(n):
        if i==0:
            prefixsub[i] = arr[i]
        else:
            prefixsub[i] = prefixsub[i-1] + arr[i]
    maxlen = 0
    hashmap = {}
    for i in range(n):
        #edge case
        if prefixsub[i] == tar:
            maxlen = max(maxlen,i+1)

        #normal case
        if prefixsub[i] not in hashmap:
            hashmap[prefixsub[i]] = i
        if (prefixsub[i] - tar) in hashmap:
            maxlen = max(maxlen,i-hashmap[prefixsub[i] - tar])
    return maxlen

arr = [2,5,3,1,2,4,1]
tar = 3
print(maxlensubarr(arr,tar))