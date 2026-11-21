#!/bin/python3

# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer
# may be null meaning that the corresponding list is empty.
#
# Example
# headA refers to 1 -> 3 -> 7 -> NULL
# headB refers to 1 -> 2 -> NULL
# The new list is 1 -> 1 -> 2 -> 3 -> 7 -> NULL
#
# Function Description
# Complete the mergeLists function in the editor below.
#
# mergeLists has the following parameters:
# - SinglyLinkedListNode pointer headA: a reference to the head of a list
# - SinglyLinkedListNode pointer headB: a reference to the head of a list
#
# Returns
# - SinglyLinkedListNode pointer: a reference to the head of the merged list
#
# Input Format
# The first line contains an integer t, the number of test cases.
#
# The format for each test case is as follows:
#
# The first line contains an integer n, the length of the first linked list.
# The next n lines contain an integer each, the elements of the linked list.
# The next line contains an integer m, the length of the second linked list.
# The next m lines contain an integer each, the elements of the second linked list.
#
# Constraints
# - 1 <= t <= 10
# - 1 <= n, m <= 1000
# - 1 <= list[i] <= 1000, where list[i] is the i^th element of the list.
#
# Sample Input
# 1
# 3
# 1
# 2
# 3
# 2
# 3
# 4
#
# Sample Output
# 1 2 3 3 4

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.merge_lists

import os

from data_structure.singly_linked_list import SinglyLinkedList, SinglyLinkedListNode
from linked_list.print_linked_list import print_singly_linked_list

def merge_lists(head1, head2):
    
    current1 = head1
    current2 = head2
    
    dummy = SinglyLinkedListNode(0)
    head = dummy
    
    while current1 is not None or current2 is not None:
        
        if current1 is None:
            dummy.next = current2
            current2 = current2.next
        
        elif current2 is None:
            dummy.next = current1
            current1 = current1.next
        
        else:
            if current1.data <= current2.data:
                dummy.next = current1
                current1 = current1.next
            else:
                dummy.next = current2
                current2 = current2.next
            
        dummy = dummy.next

    return head.next

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        test_case_count = int(input().strip())
        
        for _ in range(test_case_count):
            count = int(input().strip())
            
            list1 = SinglyLinkedList()
            
            for _ in range(count):
                list1.insert_node(int(input().strip()))
                
            count = int(input().strip())
                        
            list2 = SinglyLinkedList()
            
            for _ in range(count):
                list2.insert_node(int(input().strip()))
                
            head = merge_lists(list1.head, list2.head)
            
            print_singly_linked_list(head)
