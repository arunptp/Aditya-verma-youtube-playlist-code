class Solution:
    
    
    def equalPartition(self, N, arr):
        
        sum_arr = sum(arr)
        
        if (sum_arr%2 != 0):
            return 0
            
        sum_arr = sum_arr//2
            
        t =[[0 for j in range(0,sum_arr+1)] for i in range(0,N+1)]
        
        for i in range(0,N+1):
            t[i][0] = 1
        
        for i in range(1,N+1):
            for j in range(1, sum_arr+1):
                
                if(arr[i-1] <= j):
                    
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                    
                else:
                    
                    t[i][j] = t[i-1][j]
                    
        return t[N][sum_arr]
