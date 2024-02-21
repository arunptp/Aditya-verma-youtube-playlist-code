https://www.geeksforgeeks.org/perfect-sum-problem/#practice

# arr[i] can also be 0. 

class Solution:
	def perfectSum(self, arr, n, sum):
	    
	    MOD = int(1e9 + 7)
		
		t = [[0 for x in range(0,sum+1)] for x in range(0,n+1)]
		
		t[0][0] = 1
		    
		for i in range (1, n+1):
		    for j in range(0, sum+1):
		        
		        if(arr[i-1]<=j):
		            
		            t[i][j] = ( t[i-1][j-arr[i-1]] + t[i-1][j] ) % MOD
		            
		        else:
		            
		            t[i][j] = t[i-1][j] 
		            
	    return t[n][sum] % MOD
