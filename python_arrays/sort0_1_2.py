#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
class Solution:
    def sort012(self,arr,n):
        # code here
        i = 0
        j = 0
        while j<n:
            if arr[j] > 0:
                pass
            else:
                arr[j],arr[i] = arr[i],arr[j]
                i+=1
            j+=1
        l = i
        while l<n:
            
            if arr[l] > 1:
                pass
            else:
                arr[l],arr[i] = arr[i],arr[l]
                i+=1
            l+=1
