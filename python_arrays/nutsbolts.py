def matchPairs(self,nuts, bolts, n):
		# code here
		
        hash1 = {}
 
       # creating a hashmap
        # for nuts
        for i in range(n):
            hash1[nuts[i]] = i
 
        # searching for nuts for
        # each bolt in hash map
        for i in range(n):
            if (bolts[i] in hash1):
                nuts[i] = bolts[i]