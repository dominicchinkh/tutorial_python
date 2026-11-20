#!/bin/python3

# # A left rotation operation on a circular array shifts each of the array's elements 1 unit to the left.
# The elements that fall off the left end reappear at the right end.
# Given an integer d, rotate the array that many steps to the left and return the result.
#
# Example
# d = 2
# arr = [1, 2, 3, 4, 5]
#
# After 2 rotations, arr' = [3, 4, 5, 1, 2].
#
# Function Description
# Complete the rotateLeft function with the following parameters:
# - int d: the amount to rotate by
# - int arr[n]: the array to rotate
#
# Returns
# - int[n]: the rotated array
#
# Input Format
# The first line contains two space-separated integers that denote n, the number of integers, and d,
# the number of left rotations to perform.
# The second line contains n space-separated integers that describe arr[].
#
# Constraints
# - 1 <= n <= 10^5
# - 1 <= d <= n
# - 1 <= a[i] <= 10^6
#
# Sample Input
# STDIN   Function
# -----   --------
# 5 4     n = 5 d = 4
# 1 2 3 4 5 arr = [1, 2, 3, 4, 5]
#
# Sample Output
# 5 1 2 3 4

# OUTPUT_PATH=/dev/stdout python3 rotate_left.py

import os

def rotateLeft(d, arr):
    if not arr:
        return []
    
    d = d % len(arr)
    return arr[d:] + arr[:d]

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        first_multiple_input = input().strip().split()
        
        n = int(first_multiple_input[0])
        d = int(first_multiple_input[1])
        
        arr = list(map(int, input().strip().split()))
        
        result = rotateLeft(d, arr)
    
        file.write(' '.join(map(str, result)))
        file.write('\n')
