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

def designer_door_mat(n, m):
    
    lines = []
    for i in range(n // 2):
        lines.append(''.join(['.|.'] * (2 * i + 1)).center(m, '-'))
    
    print(
        '\n'.join(
            lines + 
            [ 'WELCOME'.center(m, '-') ] +
            lines[::-1]
        )
    )

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    designer_door_mat(n, m)
