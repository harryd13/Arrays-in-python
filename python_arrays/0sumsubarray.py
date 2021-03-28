#Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

def maxLen(n, arr):
    maxlen = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=arr[j]
            if sum == 0:
                maxlen = max(maxlen,j-i+1)
    return maxlen
   
#logic
#prefix(i) = arr[0] + arr[1] +...+ arr[i] 
#prefix(j) = arr[0] + arr[1] +...+ arr[j], j>i 
#ifprefix(i) == prefix(j) then prefix(j) - prefix(i) = 0 that means arr[i+1] + .. + arr[j] = 0, So a sub-array has zero sum , and the length of that sub-array is j-i+1 

def maxLen(n, arr):
    hash_map = {}
    sum = 0
    maxlen = 0
    if n==1 and arr[0] == 0:
        maxlen = 1
    #get commulative sum, and put any new value of sum in hash
    else:
        for i in range(n):
            sum += arr[i]
            if sum is 0:
                maxlen = i+1 # 1 2 3 -1 -2 -3
            if sum in hash_map:
                maxlen = max(maxlen,i-hash_map[sum])
            else:
                hash_map[sum] = i
    return maxlen