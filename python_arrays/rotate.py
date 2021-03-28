def rotate( arr, n):
    temp = arr[len(arr)-1]
    
    for i in range(len(arr)):
        arr[len(arr) - i-1] = arr[len(arr)-i-2]
    arr[0] = temp
    return arr
    