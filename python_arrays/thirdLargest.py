#Given an array of distinct elements. Find the third largest element in it. in ORDER N

def thirdLargest(self,arr, n):
        # code here
        if n < 3:
            return -1
        else:
            frst = 0
            scnd = 0
            thrd = 0
            for num in arr:
                if num > frst:
                    thrd = scnd
                    scnd = frst
                    frst = num
                if num>scnd and num<frst:
                    thrd = scnd
                    scnd = num
                if num>thrd and num<scnd:
                    thrd = num
                    
                else:
                    pass
            return thrd