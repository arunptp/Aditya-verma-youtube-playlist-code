03 Knapsack Bottom up.cpp

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        t = [[0 for x in range(0,W+1)] for x in range(0,n+1)]
        
        for i in range(0, n+1):
            for j in range(0, W+1):
                
                if (i==0 or j==0):
                    t[i][j] = 0
                    
                elif(wt[i-1] <= j):
                    
                    t[i][j] = max( val[i-1]+t[i-1][j-wt[i-1]] , t[i-1][j])
                    
                else:
                    
                    t[i][j] = t[i-1][j]
                    
        return t[n][W]
                
        
        print(t)
