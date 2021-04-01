t= int(input())
while t>0:
    t-=1
    n = int(input())
    l = list(map(int,input().strip().split(" ")))
    k = int(input())
    ans = []
    flag = 1
    for i in range(0,n-k+1):
        for j in range(i,i+k):
            flag = 1
            if l[j] < 0:
                ans.append(l[j])
                break
            else:
                flag = 0
        if flag == 0:
            ans.append(0)
            flag = 1
            
    print(*ans)  