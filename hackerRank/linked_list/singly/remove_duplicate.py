#!/bin/python3

# You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in
# ascending order. Delete nodes and return a sorted list with each distinct value in the original list. The given
# head pointer may be null indicating that the list is empty.
#
# Example
# head refers to the first node in the list 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 3 -> NULL.
# Remove 1 of the 2 data values and return head pointing to the revised list 1 -> 2 -> 3 -> NULL.
#
# Function Description
# Complete the removeDuplicates function in the editor below.
#
# removeDuplicates has the following parameter:
# - SinglyLinkedListNode pointer head: a reference to the head of the list
#
# Returns
# - SinglyLinkedListNode pointer: a reference to the head of the revised list
#
# Input Format
# The first line contains an integer t, the number of test cases.
#
# The format for each test case is as follows:
#
# The first line contains an integer n, the number of elements in the linked list.
# Each of the next n lines contains an integer, the data value for each of the elements of the linked list.
#
# Constraints
# - 1 <= t <= 10
# - 1 <= n <= 1000
# - 1 <= list[i] <= 1000
#
# Sample Input
# STDIN   Function
# -----   --------
# 1       t = 1
# 5       n = 5
# 1       data values = 1, 2, 2, 3, 4
# 2
# 2
# 3
# 4
#
# Sample Output
# 1 2 3 4

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.delete_node

import os

from data_structure.singly_linked_list import SinglyLinkedList
from linked_list.print_linked_list import print_singly_linked_list

def remove_duplicate(head):
    current = head
    
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        test_case_count = int(input().strip())
        
        for _ in range(test_case_count):
            count = int(input().strip())
            
            l = SinglyLinkedList()
            
            for _ in range(count):
                l.insert_node(int(input().strip()))
                
            head = remove_duplicate(l.head)
            
            print_singly_linked_list(head)
