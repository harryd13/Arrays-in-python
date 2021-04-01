from collections import deque
t= int(input())
while t>0:
    t-=1
    n = int(input())
    l = list(map(int,input().strip().split(" ")))
    k = int(input())
    ans = []
    di = deque()
    i = 0
    j = 0
    while j<n:
        if l[j]<0:
            di.append(l[j])
        if((j+1-i)<k):
            j+=1
        elif (j+1-i)==k:
            if (not di):
                ans.append(0)
            else:
                ans.append(di[0])
                if l[i] == di[0]:
                    di.popleft()
            i+=1
            j+=1   
    
        
            
    print(*ans)  
    