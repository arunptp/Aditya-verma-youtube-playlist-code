class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        
        t =  [[0 for _ in range(n+1)] for _ in range(m+1)]
         
        for i in range(1,m+1):
            for j in range(1,n+1):
                 
                if(X[i-1] == Y[j-1]):
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
            
            
        return m + n - t[m][n]
                    
                 
                    
