def minimumPlatform(self,n,arr,dep):
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    dep[j], dep[j+1] = dep[j+1], dep[j]
       
        count = 1
        plt = 1
        for i in range(0,n-1):
            plt-=1
            #check if when a train arrives we have some count or notif not add1 and sub 1 if it is in use
            if(dep[i]>=arr[i+1]):
                if(plt>0):
                    pass
                else:
                    count+=1
                    plt=count
            else:
                plt+=1
        return count
        
#optimized...
def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        plat_needed = 1
        result = 1
        i = 1
        j = 0
        while (i < n and j < n):
   
            # If next event in sorted
            # order is arrival, increment count of platforms needed
            if (arr[i] <= dep[j]):
        
                plat_needed+= 1
                i+= 1
        
 
            # Else decrement count
            # of platforms needed
            elif (arr[i] > dep[j]):
        
                plat_needed-= 1
                j+= 1

            # Update result if needed 
            if (plat_needed > result): 
                result = plat_needed
        
        return result