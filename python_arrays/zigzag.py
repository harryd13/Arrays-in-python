#Given an array Arr (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion. The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in the output i.e you have to iterate on the original array only.


def zigZag(self,arr, n):
		# code here
		for i in range(n-1):
		    if i%2==0 and arr[i]>arr[i+1]:
		        t=arr[i]
		        arr[i]=arr[i+1]
		        arr[i+1]=t
		    if i%2!=0 and arr[i]<arr[i+1]:
		        t=arr[i]
		        arr[i]=arr[i+1]
		        arr[i+1]=t
		        
	    return arr