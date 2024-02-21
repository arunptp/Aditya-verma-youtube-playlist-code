https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1

class Solution:
	def minDifference(self, arr, n):
		
		sumarr = sum(arr)
		
		t =[[0 for _ in range(sumarr+1)] for _ in range(n+1)]
		
		for i in range(0,n+1):
		    t[i][0]=1
		    
		for i in range(1,n+1):
		    for j in range(1,sumarr+1):
		        
		        if(arr[i-1]<=j):
		            
		            t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
		        else:
		            t[i][j] = t[i-1][j]
		            
		v =[]

    
		for j in range(0,sumarr//2+1): # Be careful - Took up an hour for me
		    
		    if(t[n][j] == 1):
		        v.append(j)
		'''       
		diff = []
		
		for ele in v:
		    diff.append(sumarr - 2* ele)
	    
		return min(diff)
		
		Time Efficiency: Both approaches have a similar time complexity, iterating over each element of the list once. 
		However, the first snippet has an additional overhead of creating a list and then finding the minimum, which might
		make it slightly slower due to the overhead of list creation and the separate min function call.
		
    Readability and Pythonic Practices: The first snippet is more Pythonic due to its use of list comprehensions
    and built-in functions, which are encouraged for their readability and succinctness. However, the second snippet 
    is also clear and uses a common pattern for finding minimums, making it easily understandable.
		
		'''
		    
		min_result = float('inf')
		        
		for i in range(len(v)):
		    current_result = sumarr - 2 * v[i]
		    if current_result < min_result:
		        min_result = current_result
		        
		return min_result
