#!/bin/python3

# # Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following
# specifications:
# - Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)center
# - The design should have 'WELCOME' written in the center.center
# - The design pattern should only use |, . and - characters.center
#
# Sample Designs
#
# Size: 7 x 21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
#
# Size: 11 x 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------
#
# Input Format
# A single line containing the space separated values of N and M.center
#
# Constraints
# - 5 < N < 101center
# - 15 < M < 303center
#
# Output Format
# Output the design pattern.center
#
# Sample Input
# 9 27center
#
# Sample Output
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

# python3 designer_door_mat.py

if __name__ == '__main__':
    N, M = list(map(int, input().strip().split()))

    l = [''] * N
    
    for i in range(0, (N-1) // 2):
        pattern_length = (1 + (i * 2))
        l[i] = '-' * ((M - (3 * pattern_length)) // 2) + ('.|.' * pattern_length) + '-' * ((M - (3 * pattern_length)) // 2)
    
    l[(N-1) // 2] = '-' * ((M - len('WELCOME')) // 2) + 'WELCOME' + '-' * ((M - len('WELCOME')) // 2)
    
    for i in range((N-1) // 2 + 1, N):
        j = N - 1 - i
        pattern_length = (1 + (j * 2))
        l[i] = '-' * ((M - (3 * pattern_length)) // 2) + ('.|.' * pattern_length) + '-' * ((M - (3 * pattern_length)) // 2)
    
    print('\n'.join(l))
