def transitionPoint(arr, n):
    #Code here
    l = 0
    r = n-1
    mid = n-1
    while(l<=r):
        mid = (l+r)//2
        if (mid==n-1 or mid == 0):
            if arr[mid]==1:
                return mid
            else:
                return -1
        else:
            if arr[mid+1] ==0:
                #still in 0 part
                l = mid+1
            elif arr[mid-1]==1:
                r = mid-1
            elif arr[mid-1] == 0 and arr[mid+1]==1 and arr[mid]==0:
                return mid+1
            elif arr[mid-1] == 0 and arr[mid+1]==1 and arr[mid]==1:
                return mid