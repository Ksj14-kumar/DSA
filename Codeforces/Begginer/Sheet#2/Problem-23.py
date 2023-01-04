

t= int(input())


l=[]
for i in range(t):
    length= int(input())
    array= list(map(int,input().split()[:length]))
    l.append((length,array))




def solve(n, a):
  # Initialize dp array with all values set to -1
  dp = [[-1 for _ in range(230)] for _ in range(n)]

  # Define a recursive function to calculate the minimum number of elimination operations needed
  # to make all elements in the array equal to 0, starting at index i with the given bitwise AND value j
  def dfs(i, j):
    # If dp[i][j] has already been calculated, return the stored value
    if dp[i][j] != -1:
      return dp[i][j]
    # If j is 0, then no more elimination operations are needed
    if j == 0:
      return 0
    # Initialize the minimum number of elimination operations needed to be the maximum possible value
    min_ops = float('inf')
    # For each value of k from 1 to n - i,
    for k in range(1, n - i + 1):
      # Calculate the bitwise AND of all elements from i + k to the end of the array
      next_j = a[i + k - 1]
      for l in range(i + k, n):
        next_j &= a[l]
      # Calculate the minimum number of elimination operations needed to make all elements in the array equal to 0, starting at index i + k with the next value of j
      ops = dfs(i + k, next_j)
      # If the number of elimination operations needed is less than the current minimum, update the minimum value
      if ops < min_ops:
        min_ops = ops
    # Store the minimum number of elimination operations needed in dp[i][j] and return it
    dp[i][j] = min_ops + 1
    return dp[i][j]

  # Initialize the result set to be empty
  res = set()
  # Calculate the bitwise AND of all elements in the array
  j = a[0]
  for i in range(1, n):
    j &= a[i]
  # Find the minimum number of elimination operations needed to make all elements in the array equal to 0, starting at index 0 with the initial value of j
  min_ops = dfs(0, j)
  # For each value of k from 1 to n,
  for k in range(1, n + 1):
    # Calculate the bitwise AND of all elements from k to the end of the array
    next_j = a[k - 1]
    for l in range(k, n):
      next_j &= a[l]
    # If the minimum number of elimination operations needed is equal to the current value of k, add it to the result set
    if dfs(k, next_j) == min_ops:
      res.add(k)
  # Print all values of k in the result set
  for k in res:
    print(k)

# Test the solution on the given example
solve(4, [3, 7, 1, 5])

for a,b in l:
    solve(a,b)
