#!/bin/python3

# Given a pointer to the head of a singly-linked list, print each data value from the reversed list. If the given list is empty,
# do not print anything.
#
# Example
# head* refers to the linked list with data values 1 -> 2 -> 3 -> NULL
#
# Print the following:
# 3
# 2
# 1
#
# Function Description
# Complete the reversePrint function in the editor below.
#
# reversePrint has the following parameters:
# - SinglyLinkedListNode pointer head: a reference to the head of the list
#
# Prints
# The data values of each node in the reversed list.
#
# Input Format
# The first line of input contains t, the number of test cases.
#
# The input of each test case is as follows:
# - The first line contains an integer n, the number of elements in the list.
# - Each of the next n lines contains a data element for a list node.
#
# Constraints
# - 1 <= n <= 1000
# - 1 <= list[i] <= 1000, where list[i] is the i^th element in the list.
#
# Sample Input
# 3
# 5
# 16
# 12
# 4
# 2
# 5
# 3
# 7
# 3
# 9
# 5
# 5
# 1
# 18
# 3
# 13
#
# Sample Output
# 5
# 2
# 4
# 12
# 16
# 9
# 3
# 7
# 13
# 3
# 18
# 1
# 5

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.reverse_print

from data_structure.singly_linked_list import SinglyLinkedList

def reverse_print(node):
    if node is None:
        return

    reverse_print(node.next)
    print(node.data)
    
if __name__ == '__main__':
    test_case_count = int(input().strip())
    
    for _ in range(test_case_count):
        count = int(input().strip())
        
        l = SinglyLinkedList()
        
        for _ in range(count):
            l.insert_node(int(input().strip()))
        
        reverse_print(l.head)
