def count(self,arr, n, x):
		# code here
		i = 0
		j = n-1
		start= 0
		end = 0
		mid = n-1
		#get starting pt where arr[mid]==x, arr[mid-1] <x
		while (i<=j):
		    mid = (i+j)//2
		    if arr[mid]==x:
                start=mid
                j=mid-1
            elif arr[mid]>x:
                j=mid-1
            else:
                i=mid+1
        l = 0
		r = n-1
		while (l<=r):
            mid = (l+r)//2
	        if arr[mid] == x:
	            end = mid
	            l+=1
	        elif arr[mid] > x:
	            r = mid-1
	        else:
	            l = mid+1
	    if end==start:
	        if arr[end] == x:
	            return 1
	        else:
	            return 0
	    else:
            return end-start+1