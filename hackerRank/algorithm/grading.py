#!/bin/python3

# HackerLand University has the following grading policy:
# - Every student receives a grade in the inclusive range from 0 to 100.
# - Any grade less than 40 is a failing grade.
#
# Sam is a professor at the university and likes to round each student's grade
# according to these rules:
# - If the difference between the grade and the next multiple of 5 is less than 3,
#   round grade up to the next multiple of 5.
# - If the value of grade is less than 38, no rounding occurs as the result will still
#   be a failing grade.
#
# Examples
# - grade = 84 round to 85 (85 - 84 is less than 3)
# - grade = 29 do not round (result is less than 38)
# - grade = 57 do not round (60 - 57 is 3 or higher)
#
# Given the initial value of grade for each of Sam's n students, write code to
# automate the rounding process.
#
# Function Description
# Complete the function gradingStudents with the following parameter(s):
# - int grades[n]: the grades before rounding
#
# Returns
# - int[n]: the grades after rounding
#
# Input Format
# The first line contains a single integer, n, the number of students.
# Each line i of the n subsequent lines contains a single integer, grades[i].
#
# Constraints
# - 1 <= n <= 60
# - 0 <= grades[i] <= 100
#
# Sample Input 0
# 4
# 73
# 67
# 38
# 33
#
# Sample Output 0
# 75
# 67
# 40
# 33

# OUTPUT_PATH=/dev/stdout python3 grading.py

import os

def grading_students(grades):
    return [
        g + (5 - g % 5) if g >= 38 and g % 5 >= 3 else g
        for g in grades
    ]

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        count = int(input().strip())
        
        grades = []
        
        for _ in range(count):
            grades.append(int(input().strip()))
        
        result = grading_students(grades)
        
        file.write('\n'.join(map(str, result)))
        file.write('\n')
