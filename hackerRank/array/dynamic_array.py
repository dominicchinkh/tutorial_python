#!/bin/python3

# - Declare a 2-dimensional array, arr, with n empty arrays, all zero-indexed.
# - Declare an integer, lastAnswer, and initialize it to 0.
#
# You need to process two types of queries:
# 1. Query: 1 x y
#   o Compute idx = (x XOR lastAnswer).
#   o Append the integer y to arr[idx].
# 2. Query: 2 x y
#   o Compute idx = (x XOR lastAnswer).
#   o Set lastAnswer = arr[idx][y % size(arr[idx])].
#   o Store the new value of lastAnswer in an answers array.
#
# Notes:
# - XOR is the bitwise XOR operation, which corresponds to the ^ operator in
#   most languages. Learn more about it on Wikipedia.
# - % is the modulo operator.
# - Finally, size(arr[idx]) is the number of elements in arr[idx].
#
# Function Description
# Complete the dynamicArray function with the following parameters:
# - int n: the number of empty arrays to initialize in arr
# - int queries[q][3]: 2-D array of integers
#
# Returns
# - int[]: the results of each type 2 query in the order they are presented
#
# Input Format
# The first line contains two space-separated integers, n, the size of arr to
# create, and q, the number of queries, respectively.
# Each of the q subsequent lines contains a query string, queries[i].
#
# Constraints
# - 1 <= n, q <= 10^5
# - 0 <= x, y <= 10^9
# - It is guaranteed that query type 2 will never query an empty array or
#   index.
#
# Sample Input
# STDIN   Function
# -----   --------
# 2 5     size of arr[] n = 2, size of queries[] q = 5
# 1 0 5   queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
# 1 1 7
# 1 0 3
# 2 1 0
# 2 1 1
#
# Sample Output
# 7
# 3

# OUTPUT_PATH=/dev/stdout python3 dynamic_array.py

import os

def dynamicArray(n, queries):
    arr = [ [] for _ in range(n) ]
    last_answer = 0
    answers = []
    
    for query_type, x, y in queries:
        idx = (x ^ last_answer) % n
        
        if query_type == 1:
            arr[idx].append(y)
            
        elif query_type == 2:
            last_answer = arr[idx][y % len(arr[idx])]
            answers.append(last_answer)
    
    return answers

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        first_multiple_input = input().strip().split()
        
        n = int(first_multiple_input[0])
        q = int(first_multiple_input[1])
        
        queries = []
        
        for _ in range(q):
            queries.append(list(map(int, input().strip().split())))
            
        result = dynamicArray(n, queries)
        
        file.write('\n'.join(map(str, result)))
        file.write('\n')
