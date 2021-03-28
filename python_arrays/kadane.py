 def maxSubArraySum(self,a,size):
        ##Your code here
        n = size
        cur_sum = 0
        mx_sum = a[0]
        for i in range(n):
            cur_sum+=a[i]
            if (mx_sum<cur_sum):
                mx_sum = cur_sum
            if cur_sum<0:
                cur_sum = 0
        return mx_sum
