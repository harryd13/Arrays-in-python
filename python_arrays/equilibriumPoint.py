def equilibriumPoint(A, N):
        # Your code here
        sm = sum(A)
        left_sum = 0
        right_sum = sm
        for i in range(N):
            right_sum-=A[i]
            if(left_sum==right_sum):
                return i+1
            left_sum+=A[i]
        return -1