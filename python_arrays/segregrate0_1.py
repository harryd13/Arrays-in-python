#Given an array of length N consisting of only 0s and 1s in random order. Modify the array to segregate 0s on left side and 1s on the right side of the array.
def segregate0and1(self, arr, n):
        # code here
        i = 0
        j = 0
        while j<n:
            if arr[j]==0:
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
            else:
                pass
            j+=1
