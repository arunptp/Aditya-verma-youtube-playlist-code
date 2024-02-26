class Solution:
    def count(self, coins, N, Sum):
        
        t = [[0 for _ in range(0,Sum+1)] for _ in range(0,N+1)]
        
        for i in range(0, N+1):
            t[i][0] = 1
        
        for i in range(1, N+1):
            for j in range(1, Sum+1):
                
                if(coins[i-1]<=j):
                    
                    t[i][j] = t[i-1][j] + t[i][j - coins[i-1]]
                    
                else:
                    
                    t[i][j] = t[i-1][j]
        
        return t[N][Sum]
