#!/bin/python3

# Given a 6 x 6 2D array, arr, an hourglass is a subset of values with indices falling in the
# following pattern:
#
# a b c
#   d
# e f g
#
# There are 16 hourglasses in a 6 x 6 array. The hourglass sum is the sum of the values
# in an hourglass. Calculate the hourglass sum for every hourglass in arr, then print the
# maximum hourglass sum.
#
# Example
# arr =
#
# -9 -9 -9  1 1 1
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
#
# The 16 hourglass sums are:
#
# -63, -34, -9, 12,
# -10,   0, 28, 23,
# -27, -11, -2, 10,
#   9,  17, 25, 18
#
# The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:
#
# 0 4 3
#   1
# 8 6 6
#
# Note: If you have already solved the Java domain's Java 2D Array challenge, you may
# wish to skip this challenge.
#
# Function Description
# Complete the function hourglassSum with the following parameter(s):
# - int arr[6][6]: a 2-D array of integers
#
# Returns
# - int: the maximum hourglass sum
#
# Input Format
# Each of the 6 lines of inputs arr[i] contains 6 space-separated integers arr[i][j].
#
# Constraints
# - -9 <= arr[i][j] <= 9
# - 0 <= i, j <= 5
#
# Sample Input
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
#
# Sample Output
# 19

# OUTPUT_PATH=/dev/stdout python3 reverse_array.py

import os

def hourglassSum(a):
    max_sum = float('-inf')
    
    for r in range(4):
        for c in range(4):
            current_sum = (
                a[r  ][c] + a[r  ][c+1] + a[r  ][c+2] +
                            a[r+1][c+1] +
                a[r+2][c] + a[r+2][c+1] + a[r+2][c+2]
            )
            if current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        a = []
        
        for _ in range(6):
            a.append(list(map(int, input().rstrip().split())))

        result = hourglassSum(a)
        
        file.write(str(result) + '\n')