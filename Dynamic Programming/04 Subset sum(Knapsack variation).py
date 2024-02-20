class Solution:
    
    def isSubsetSum (self, N, arr, sum):
        
        t = [[0 for x in range(0, sum+1)] for x in range(0, N+1)]
        
        
        for i in range(N + 1):
            t[i][0] = 1
        
        for i in range (1, N+1):
            for j in range (1,sum+1):
                
 
                if(arr[i-1] <= j):
                    
                    t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
                    
                else:
                
                    t[i][j] = t[i-1][j]
                    
        return t[N][sum]
