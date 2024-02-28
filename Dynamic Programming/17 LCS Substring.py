class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        
        t = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            
            for j in range(1,m+1):
                
                if(S1[i-1] == S2[j-1]):
                    
                    t[i][j] = 1 + t[i-1][j-1]
                    
                else:
                    t[i][j] = 0
                    
        return max(max(row) for row in t)
