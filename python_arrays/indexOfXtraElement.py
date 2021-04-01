def findExtra(a,b,n):
        
        #add code here
        l = 0
        r= n-1
        
        while(l<=r):
            mid = (l+r)//2
            if mid==n-1:
                ans = n-1
                break
            if a[mid] == b[mid]:
                l = mid+1
                
            else:
                if(a[mid-1] == b[mid-1]):
                    ans = mid
                    break
                else:
                    r = mid-1
        return ans