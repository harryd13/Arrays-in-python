#Given an array H representing heights of buildings. You have to count the buildings which will see the sunrise (Assume : Sun rise on the side of array starting point).

def countBuildings(h, n):
        # code here
        #logic -- thos will see the sunrise which have all the elements before them smaller
        count = 1
        for i in range(0,len(h)-1):
            if(h[i+1]<=h[i]):
                t = h[i]
                h[i] = h[i+1]
                h[i+1] = t
            else:
                count+=1
        return count