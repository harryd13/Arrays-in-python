t = int(input())
while t>0:
    par= list(map(int,input().split(" ")))
    n = par[0]
    d= par[1]
    arr = list(map(int,input().strip().split(" ")))
    l = [0 for i in range(n)]
    for i in range(0,n):
        l[i] = arr[(d+i)%n]
    print(*l)#newthinglearnt
    t-=1
     