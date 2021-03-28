def countZeroes(self,arr, n):
        # code here
        l=0
        r=n-1
        pos=n
        while(l<=r):
            mid=(l+r)//2
            if arr[mid]==0 and (mid==0 or arr[mid-1]==1):
                pos=mid
                break
            elif arr[mid]==1 :
                l=mid+1
            else :
                r=mid-1
        return(n-pos)