#Given an array Arr of N positive integers and a number K where K is used as a threshold value to divide each element of the array into sum of different numbers. Find the sum of count of the numbers in which array elements are divided.

def totalCount(self, arr, n, k):
        # code here
        count = 0
        for nmbr in arr:
            if nmbr%k == 0:
                count+=(nmbr//k) 
            else:
                count+=(nmbr//k)+1
        return count