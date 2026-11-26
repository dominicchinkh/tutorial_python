#!/bin/python3

# ABC is a right triangle, 90° at B.
# Therefore, ∠ABC = 90°.
#
# Point M is the midpoint of hypotenuse AC.
#
# You are given the lengths AB and BC.
# Your task is to find ∠MBC (angle θ°, as shown in the figure) in degrees.
#
# Input Format
#
# The first line contains the length of side AB.
# The second line contains the length of side BC.
#
# Constraints
# - 0 < AB <= 100
# - 0 < BC <= 100
# - Lengths AB and BC are natural numbers.
#
# Output Format
#
# Output ∠MBC in degrees.
#
# Note: Round the angle to the nearest integer.
#
# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.
#
# 0° < θ° < 90°
#
# Sample Input
# 10
# 10
#
# Sample Output
# 45°

# Step-by-Step Geometric Proof
#
# 1. Right triangle and midpoint: Triangle ABC has a 90° angle at B, and M is the 
#    midpoint of hypotenuse AC.
#
# 2. Median to the hypotenuse: A standard theorem of Euclidean geometry states that 
#    the median drawn from the right angle (B) to the midpoint (M) of the hypotenuse 
#    (AC) is half as long as the hypotenuse: 
#
#      BM = (1/2) * AC.
#
# 3. Equal segments on the hypotenuse: Since M is the midpoint of AC, both halves also
#    equal half the hypotenuse: AM = MC = (1/2) * AC.
#
# 4. Isosceles triangle MBC: Comparing sides BM and MC gives BM = MC. Because two sides
#    of triangle MBC are equal, triangle MBC is isosceles.
#
# 5. Equal base angles: Angles opposite equal sides in a triangle are equal, so the 
#    angles opposite MC and BM are equal: ∠MBC = ∠MCB.
#
# 6. Same angle, different name: Vertices M, C, and A are collinear along the hypotenuse 
#    AC, so ∠MCB and ∠ACB are the exact same angle: ∠MBC = ∠ACB.

# OUTPUT_PATH=/dev/stdout python3 find_angle.py 

import math

from decimal import Decimal, ROUND_HALF_UP

if __name__ == '__main__':
    ab, bc = int(input()), int(input())

    angle_deg = math.degrees(math.atan2(ab, bc))
    rounded = int(Decimal(str(angle_deg)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    print(f"{rounded}\u00b0")
