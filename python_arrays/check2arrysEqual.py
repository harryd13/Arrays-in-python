def check(self,A,B,N):
        
        #return: True or False
        count0 = 0
        #code here
        h_map = {}
        for i in range(N):
            if A[i] not in h_map:
                h_map[A[i]] = 1
            elif A[i] in h_map:
                h_map[A[i]]+=1
        #print(h_map)
        for i in range(N):
            if B[i] not in h_map:
                return False
            elif B[i] in h_map:
                h_map[B[i]]-=1
        #print(h_map)
        for i in range(N):
            if h_map[A[i]] != 0:
                count0 = 1
        if count0 == 0:
            return True
        else:
            return False
