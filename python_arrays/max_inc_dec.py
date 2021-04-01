#Given an array Arr of N elements which is first increasing and then may be decreasing, find the maximum element in the array.

def findMaximum(self,arr, n):
		# code here
		l = 0
		r = n-1
		mid = n-1
		while(l<=r):
		    mid = (r+l)//2
		    if(mid == n-1  or mid == 0):
		        return arr[mid]
		       
		    else:
    		    if arr[mid+1]>arr[mid]:
    		        l = mid+1
    		    elif arr[mid+1]<arr[mid] and arr[mid-1]>arr[mid]:
    		        r = mid-1
    		    elif (arr[mid+1]<arr[mid] and arr[mid-1]<arr[mid]):
    		        return arr[mid]