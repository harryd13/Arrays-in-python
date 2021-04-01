def rearrange(arr, n): 
        ##Your code here
        l = 0
        r = n-1
        mx = arr[n-1]+1
        for i in range(n):
            if i%2 == 0:
                arr[i]+=(arr[r]%mx)*mx
                r -= 1
            else:
                arr[i]+=(arr[l]%mx)*mx
                l += 1
        for i in range(n):
            arr[i] = arr[i]//mx
        return arr