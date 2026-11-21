#!/bin/python3

# Given the pointer to the head node of a doubly linked list, reverse the order
# of the nodes in place. That is, change the next and prev pointers of the
# nodes so that the direction of the list is reversed. Return a reference to the
# head node of the reversed list.
#
# Note: The head node might be NULL to indicate that the list is empty.
#
# Function Description
# Complete the reverse function in the editor below.
#
# reverse has the following parameter(s):
# - DoublyLinkedListNode head: a reference to the head of a
#   DoublyLinkedList
#
# Returns
# - DoublyLinkedListNode: a reference to the head of the reversed list
#
# Input Format
# The first line contains an integer t, the number of test cases.
#
# Each test case is of the following format:
# - The first line contains an integer n, the number of elements in the linked
#   list.
# - The next n lines contain an integer each denoting an element of the
#   linked list.
#
# Constraints
# - 1 <= t <= 10
# - 0 <= n <= 1000
# - 0 <= DoublyLinkedListNode.data <= 1000
#
# Output Format
# Return a reference to the head of your reversed list. The provided code will
# print the reverse array as a one line of space-separated integers for each
# test case.
#
# Sample Input
# 1
# 4
# 1
# 2
# 3
# 4
#
# Sample Output
# 4 3 2 1

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.doubly.reverse

import os

from data_structure.doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode
from linked_list.print_linked_list import print_doubly_linked_list

def reverse(head):
    prev = None
    current = head
    
    while current is not None:
        next = current.next
        
        current.next = prev
        current.prev = next
        
        prev = current
        current = next
    
    return prev

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        test_case_count = int(input().strip())
        
        for _ in range(test_case_count):
            count = int(input().strip())
            
            l = DoublyLinkedList()
            
            for _ in range(count):
                l.insert_node(int(input().strip()))
            
            l.head = reverse(l.head)
            
            print_doubly_linked_list(l.head, ' ', file)
            file.write('\n')
