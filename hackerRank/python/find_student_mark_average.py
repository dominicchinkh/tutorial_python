#!/bin/python3

# Overview: collections.namedtuple creates lightweight tuple-like objects with named fields
# so you can access attributes by name rather than numeric index.
#
# Task: Given N student rows with columns in any order (ID, MARKS, CLASS, NAME),
# compute the mean of MARKS across all N students and print it rounded to 2 decimal places.

# python3 find_student_mark_average.py

from collections import namedtuple

if __name__ == '__main__':
    student_number = int(input())
    
    Student = namedtuple('Student', input().strip().split())

    sum = 0    
    for _ in range(student_number):
        s = Student(*input().strip().split())
        sum += int(s.MARKS)

    print(f'{ sum / student_number:.2f}')
