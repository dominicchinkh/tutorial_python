#!/bin/python3

# Given the pointer to the head node of a linked list, change the next pointers
# of the nodes so that their order is reversed. The head pointer given may be
# null meaning that the initial list is empty.
#
# Example
# head references the list 1 -> 2 -> 3 -> NULL
#
# Manipulate the next pointers of each node in place and return head, now
# referencing the head of the list 3 -> 2 -> 1 -> NULL.
#
# Function Description
# Complete the reverse function in the editor below.
#
# reverse has the following parameters:
# - SinglyLinkedListNode pointer head: a reference to the head of a list
#
# Returns
# - SinglyLinkedListNode pointer: a reference to the head of the reversed list
#
# Input Format
# The first line contains an integer t, the number of test cases.
#
# Each test case has the following format:
#
# The first line contains an integer n, the number of elements in the linked list.
# Each of the next n lines contains an integer, the data values of the elements
# in the linked list.
#
# Constraints
# - 1 <= t <= 10
# - 1 <= n <= 1000
# - 1 <= list[i] <= 1000, where list[i] is the i^th element in the list.
#
# Sample Input
# 1
# 5
# 1
# 2
# 3
# 4
# 5
#
# Sample Output
# 5 4 3 2 1

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.reverse

import os

from data_structure.singly_linked_list import SinglyLinkedList
from linked_list.print_linked_list import print_singly_linked_list

def reverse(head):
    prev = None
    current = head
    
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
    return prev

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        test_case_count = int(input().strip())
        
        for _ in range(test_case_count):
            count = int(input().strip())
            
            l = SinglyLinkedList()
            
            for _ in range(count):
                l.insert_node(int(input().strip()))
            
            l.head = reverse(l.head)
            print_singly_linked_list(l.head)
