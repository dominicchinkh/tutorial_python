#!/bin/python3

# Starting with a 1-indexed array of zeros and a list of operations, for each
# operation add a value to each array element between two given indices,
# inclusive. Once all operations have been performed, return the maximum value
# in the array.
#
# Example
# n = 10
# queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
#
# Queries are interpreted as follows:
#
# a b k
# 1 5 3
# 4 8 7
# 6 9 1
#
# Add the values of k between the indices a and b inclusive:
#
# [0, 0, 0,  0,  0, 0, 0, 0, 0, 0]
# [3, 3, 3,  3,  3, 0, 0, 0, 0, 0]
# [3, 3, 3, 10, 10, 7, 7, 7, 0, 0]
# [3, 3, 3, 10, 10, 8, 8, 8, 1, 0]
#
# The largest value is 10 after all operations are performed.
#
# Function Description
# Complete the function arrayManipulation with the following parameters:
# - int n: the number of elements in the array
# - int queries[q][3]: a two dimensional array of queries where each
#   queries[i] contains three integers, a, b, and k.
#
# Returns
# - int: the maximum value in the resultant array
#
# Input Format
# The first line contains two space-separated integers n and q, the size of the
# array and the number of queries.
# Each of the next q lines contains three space-separated integers a, b and k,
# the left index, right index and number to add.
#
# Constraints
# - 3 <= n <= 10^7
# - 1 <= m <= 2 * 10^5
# - 1 <= a <= b <= n
# - 0 <= k <= 10^9
#
# Sample Input
# STDIN   Function
# -----   --------
# 5 3     arr[] size n = 5, queries[] size q = 3
# 1 2 100 queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
# 2 5 100
# 3 4 100
#
# Sample Output
# 200

import os

def arrayManipulation(n, queries):
    diff = [0] * (n + 2)
    
    for a, b, k in queries:
        diff[a]     += k
        diff[b + 1] -= k

    max_val = 0
    current_val = 0
    
    for i in range(1, n + 1):
        current_val += diff[i]
        if current_val > max_val:
            max_val = current_val
            
    return max_val


if __name__ == '__main__':
    
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        first_multiple_input = list(map(int, input().strip().split()))
        
        n = first_multiple_input[0]
        q = first_multiple_input[1]
        
        queries = []
        
        for _ in range(q):
            queries.append(list(map(int, input().strip().split())))
        
        result = arrayManipulation(n, queries)
        
        file.write(str(result))
        file.write('\n')
