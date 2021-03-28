def partition(arr, l,r):
    i = l-1
    j = l
    while j < r:
        if (arr[j] < arr[r-1]):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            pass
        j+=1
    arr[i+1], arr[r-1] = arr[r-1], arr[i+1]
    return i+1
    
arr = [1,3,4,6,7,2]
print(partition(arr,0,6))

def quicksort(arr,l,r):
    if(l<r):
        piv = partition(arr,l,r)
        quicksort(arr,l,piv-1)
        quicksort(arr,piv+1,r)
    
quicksort(arr,0,6)
print(arr)