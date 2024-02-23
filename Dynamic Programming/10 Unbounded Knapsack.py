https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/#practice

class Solution:
    def knapSack(self, N, W, val, wt):
        
        t = [[0 for _ in range(W+1)] for _ in range(N+1)]
        
        for i in range(1,N+1):
            
            for j in range(1,W+1):
                
                if(wt[i-1]<=j):
                    
                    t[i][j] = max(val[i-1]+t[i][j-wt[i-1]] , t[i-1][j])
                    
                else:
                    
                    t[i][j] = t[i-1][j]
                    
        return t[N][W]
