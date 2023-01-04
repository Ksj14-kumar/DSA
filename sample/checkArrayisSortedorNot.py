from collections import defaultdict

def is_sorted(a):
    for i in range(1,len(a)):
        if(a[i-1]>=a[i]):
            return False

    return True



print(-int(1e9))

# global total=0
# sum=0
# def fact(n):
#     if(n==0):
#         return 1
#     value= n*fact(n-1)
#     print("be",total,sum)
#     sum =total+n
#     print("after",total,sum)
#     return value
# total=fact(5)
# print(total)
# fact(5)
# print()

# print(defaultdict(lambda :0))
# l1= [2,4,10,]
# l1.extend(["hello","",[]])
# print(l1)
# print(list(filter(bool,l1)))

def sq(n):
    return n*n

def cube(n):
    return n*n*n
l1= [1,2,3]
s1= list(map(cube,l1))
s2=list(map(sq,s1))


# def strangrSum():
# for _ in range(int(input())):
#     n=input()
#     lst=[int(x) for x in input().split()]
#     q=int(input())
#     for j in range(q):
#         l,r=[int(x) for x in input().split()]
#         xsum=0                  #Initializing the sum variable
#         for i in range(l,r+1):  #Traverse linearly from index 'l' to 'r'
#             xsum+=lst[i-1]      #Converting to 0-based indexing and adding to sum
#         print(xsum)


# strangrSum()

# Python program to count pairs with
# maximum sum

# Python 3 program to count
# pairs with maximum sum.
import sys

# Function to find the number
# of maximum pair sums


# Python3 program to find largest  
# pair sum in a given array 
  
# Function to return largest pair  
# sum. Assumes that there are  
# at-least two elements in arr[]  
def findLargestSumPair(arr, n): 
  
    # Initialize first and second 
    # largest element 
    if arr[0] > arr[1]: 
        first = arr[0] 
        second = arr[1] 
      
    else: 
        first = arr[1] 
        second = arr[0] 
      
  
    # Traverse remaining array and  
    # find first and second largest 
    # elements in overall array 
    for i in range(2, n): 
      
        # If current element is greater 
        # than first then update both 
        # first and second  
        if arr[i] > first: 
            second = first 
            first = arr[i] 
          
  
        # If arr[i] is in between first  
        # and second then update second  
        elif arr[i] > second and arr[i] != first: 
            second = arr[i] 
      
    return (first + second) 
  
# Driver program to test above function */ 
arr = [1,2,3,4] 
n = len(arr) 
print("Max Pair Sum is",  
      findLargestSumPair(arr, n)) 
  
#   sumRange(int i, int j) {
#         int sum = 0;
#         for (int m = i; m <= j; m++) {
#             sum += nums[m];
#         }

#         return sum;
#     }



# class NumArray:

#     def __init__(self, nums):
#         self.lst = []
#         sum_ = 0
#         for i in nums:
#             sum_ += i
#             self.lst.append(sum_)

#     def sumRange(self, i: int, j: int) -> int:
#         if i > 0 and j >0:
#             return self.lst[j] - self.lst[i-1]
#         else:
#             return self.lst[j]


# b=NumArray([1,2,3])
# print(b.sumRange(1,3))



# Python3 Program to find maximum XOR
# value of a pair

# Utility function to check number of
# elements having set msb as of pattern


def checkBit(pattern, arr, n):
	count = 0

	for i in range(0, n):
		if ((pattern & arr[i]) == pattern):
			count = count + 1
	return count

# Function for finding maximum and
# value pair


def maxAND(arr, n):
	res = 0
	# iterate over total of 32bits
	# from msb to lsb
	for bit in range(31, -1, -1):
		# find the count of element
		# having set msb
		count = checkBit(res | (1 << bit), arr, n)
		# if count >= 2 set particular
		# bit in result
		if (count >= 2):
			res = res | (1 << bit)

	return res


# Driver function
arr = [2,2,3,1]
n = len(arr)
print("Maximum AND Value = ", maxAND(arr, n))








# v#include <bits/stdc++.h>
# using namespace std;
# #define MOD 998244353
# #define ll long long

# int prod(int n)
# {
#     if (n == 0)
#         return 1;
#     return (n * prod(n - 1)) % MOD;
# }

# int strangeRangeSum(int N, vector<vector<int>> ranges, int K)
# {
#     ll sum = 0;
#     ll f;
#     for (ll i = 0; i < ranges.size(); i++)
#     {
#         for (ll j = i; j < ranges.size(); j++)
#         {
#             f = 0;
#             for (ll z = 0; z < ranges.size(); z++)
#             {
#                 if (i == z)
#                     continue;
#                 for (ll a = ranges[z][0]; a <= ranges[z][1]; a++)
#                 {
#                     for (ll b = ranges[i][0]; b <= ranges[i][1]; b++)
#                     {
#                         if (z < K)
#                             f = f ^ (a | b);
#                         else
#                             f = f ^ (a & b);
#                     }
#                 }
#             }
#             sum = sum + f;
#         }
#     }
#     return sum;
# }

# int main()
# {
#     ios_base::sync_with_stdio(false);
#     cin.tie(NULL);
#     cout.tie(NULL);
#     int t;
#     cin >> t;
#     for (int i = 0; i < t; i++)
#     {
#         int n, k;
#         cin >> n >> k;
#         vector<vector<int>> ranges(n);
#         for (int j = 0; j < n; j++)
#         {
#             ranges[j].resize(2);

#             for (int k = 0; k < 2; k++)
#             {
#                 cin >> ranges[j][k];
#             }

#             cin.ignore(numeric_limits<streamsize>::max(), '\n');
#         }

#         int result = strangeRangeSum(n, ranges, k);
#         cout << result << "\n";
#     }
#     return 0;
# }
# # This code is contributed by Nikita Tiwari




# import math
# import os
# import random
# import re
# import sys

# # Complete the strangeRangeSum function below.
# def strangeRangeSum(n, ranges, k):
#     # Write your code here
#     sum = 0
#     for i in range(ranges[0][0],ranges[0][1]+1):
#         for j in range(ranges[1][0],ranges[1][1]+1):
#             for l in range(ranges[2][0],ranges[2][1]+1):
#                 if k == 1:
#                     sum += i | j
#                     sum = sum ^ l
#                 elif k == 2:
#                     sum += i | l
#                     sum = sum ^ j
#                 else:
#                     sum += j | l
#                     sum = sum ^ i
#     return sum

# if _name_ == '_main_':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         n = int(input())

#         ranges = []

#         for _ in range(n):
#             ranges.append(list(map(int, input().rstrip().split())))

#         k = int(input())

#         result = strangeRangeSum(n, ranges, k)

#         fptr.write(str(result) + '\n')

#     fptr.close()
def strangeRangeSum (N, ranges, k):

    # Write your code here
    sum = 0
    
    for i in range(ranges[0][0],ranges[0][1]+1):
        for j in range(ranges[1][0],ranges[1][1]+1):

            for l in range(ranges[2][0],ranges[2][1]+1):
                if k == 1:
                    print(sum)
                    sum += i | j
                    print(sum)
                    sum = sum ^ l
                    print(sum)

                elif k == 2:

                    sum += i | l
                    print(sum)

                    sum = sum ^ j
                    print(sum)

                else:
                    sum += j | l
                    print(sum)

                    sum = sum ^ i
                    print(sum)

    
    print(sum)
    return sum%998244353


print(strangeRangeSum(3,[ [2, 3], [2, 2], [1, 2] ] ,1))