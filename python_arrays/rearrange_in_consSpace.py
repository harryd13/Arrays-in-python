#Let's assume an element is a and another element is b, both the elements are less than n. So if an element a is incremented by b*n. So the element becomes a + b*n so when a + b*n is divided by n then the value is b and a + b*n % n is a.
def arrange(self,arr, n): 
        #a+(b*n),a = arr[i],b = arr[arr[i]]
        for i in range(n):
            arr[i] = arr[i]+((arr[arr[i]]%n)*n)#we need older val as when we updated the prev val we have to use (a+(b*n))%n
        
        for i in range(n):
            arr[i] = int(arr[i]/n)
        