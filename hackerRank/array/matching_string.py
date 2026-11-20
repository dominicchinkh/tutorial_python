#!/bin/python3

# There is a collection of input strings and a collection of query strings. For each
# query string, determine how many times it occurs in the list of input strings.
# Return an array of the results.
#
# Example
# stringList = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']
#
# There are 2 instances of 'ab', 1 of 'abc', and 0 of 'bc'. For each query, add an
# element to the return array: results = [2, 1, 0].
#
# Function Description
# Complete the function matchingStrings with the following parameters:
# - string stringList[n]: an array of strings to search
# - string queries[q]: an array of query strings
#
# Returns
# - int[q]: the results of each query
#
# Input Format
# The first line contains and integer n, the size of stringList[].
# Each of the next n lines contains a string stringList[i].
# The next line contains q, the size of queries[].
# Each of the next q lines contains a string queries[i].
#
# Constraints
# 1 <= n <= 1000
# 1 <= q <= 1000
# 1 <= |stringList[i]|, |queries[i]| <= 20 .
#
# Sample Input 1
# Array: stringList = [aba, baba, aba, xzxb]
# Array: queries = [aba, xzxb, ab]
#
# 4
# aba
# baba
# aba
# xzxb
# 3
# aba
# xzxb
# ab
#
# Sample Output 1
# 2
# 1
# 0

import os

from collections import Counter

def matchingStrings(strings, queries):
    counts = Counter(strings)
    return [ counts[q] for q in queries ]

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        strings_count = int(input().strip())
        
        strings = []
        
        for _ in range(strings_count):
            strings.append(input().strip())
        
        queries_count = int(input().strip())
        
        queries = []
        
        for _ in range(queries_count):
            queries.append(input().strip())
        
        result = matchingStrings(strings, queries)
        
        file.write(' '.join(map(str, result)))
        file.write('\n')
