def sortBinaryArray (self, arr, n):
        # Your code here
        i = -1
        j = 0
        while(j<n):
            if arr[j] == 1:
                j+=1
            else:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]
                j+=1
        return arr