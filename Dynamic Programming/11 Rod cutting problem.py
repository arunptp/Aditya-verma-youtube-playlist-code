

class Solution:
    def cutRod(self, price, n):
    
        lt = []
       
        for i in range(0, n):
           lt.append(i+1)

            
        t = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                
                if(lt[i-1] <= j):
                    
                    t[i][j] = max( price[i-1] + t[i][j-lt[i-1]] , t[i-1][j] )
                    
                else:
                    
                    t[i][j] = t[i-1][j]
                    
        return t[n][n]
