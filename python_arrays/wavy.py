def convertToWave(A,N):
        #Your code here
        A.sort()
        for i in range(0,len(A)-1,2):
            t = A[i]
            A[i] = A[i+1]
            A[i+1] = t