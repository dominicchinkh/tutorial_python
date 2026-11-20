#!/bin/python3

# An array is a data structure that stores elements of the same type in a
# contiguous block of memory. In an array, A, of size N, each memory
# location has some unique index, i (where 0 <= i < N), that can be
# referenced as A[i] or A_i.
#
# Your task is to reverse an array of integers.
#
# Example
# A = [1, 2, 3]
# Return [3, 2, 1].
#
# Function Description
# Complete the function reverseArray with the following parameter(s):
# - int A[n]: the array to reverse
#
# Returns
# - int[n]: the reversed array
#
# Input Format
# The first line contains an integer, N, the number of integers in A.
# The second line contains N space-separated integers that make up A.
#
# Constraints
# - 1 <= N <= 10^3
# - 1 <= A[i] <= 10^4, where A[i] is the ith integer in A

# OUTPUT_PATH=/dev/stdout python3 reverse_array.py

import os

def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        count = int(input().strip())
        array = list(map(int, input().rstrip().split()))
        result = reverseArray(array)
        file.write(' '.join(map(str, result)))
        file.write('\n')
