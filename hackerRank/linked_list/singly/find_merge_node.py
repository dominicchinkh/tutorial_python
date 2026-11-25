#!/bin/python3

# Given pointers to the head nodes of 2 linked lists that merge together at some point, find the node where the two lists
# merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is
# guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return
# that node's data value.
#
# Note: After the merge point, both lists will share the same node pointers.
#
# Example
# In the diagram below, the two lists converge at Node x:
#
# [List #1] a--->b--->c
#                      \
#                       x--->y--->z--->NULL
#                      /
#        [List #2] p--->q
#
# Function Description
# Complete the findMergeNode function in the editor below.
#
# findMergeNode has the following parameters:
# - SinglyLinkedListNode pointer head1: a reference to the head of the first list
# - SinglyLinkedListNode pointer head2: a reference to the head of the second list
#
# Returns
# - int: the data value of the node where the lists merge
#
# Input Format
# Do not read any input from stdin/console.
# The first line contains an integer t, the number of test cases.
# Each of the test cases is in the following format:
# The first line contains an integer index, the node number where the merge will occur.
# The next line contains an integer list1_count that is the number of nodes in the first list.
# Each of the following list1_count lines contains a data value for a node. The next line contains an integer list2_count
# that is the number of nodes in the second list.
# Each of the following list2_count lines contains a data value for a node.
#
# Constraints
# The lists will merge.
# head1, head2 != null.
# head1 != head2 .
#
# Sample Input
# The diagrams below are graphical representations of the lists that input nodes head1 and head2 are connected to.
#
# Test Case 0
# 1
#  \
#   2--->3--->NULL
#  /
# 1
#
# Test Case 1
# 1--->2
#       \
#        3--->Null
#       /
#      1
#
# Sample Output
# 2
# 3

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.delete_node

import os

from data_structure.singly_linked_list import SinglyLinkedList

# How the Two Pointers Move on This Diagram
# - List A path: a1 -> a2 -> c1 -> c2 -> c3 -> None       (2 nodes before c1, then 3 shared nodes)
# - List B path: b1 -> b2 -> b3 -> c1 -> c2 -> c3 -> None (3 nodes before c1, then 3 shared nodes)

# - Why they meet at c1: current1 starts at a1 and current2 starts at b1.
#   Whenever either pointer hits None, it jumps to the head of the other list (head2 or head1).
#   Because list A has 1 fewer node before c1, current1 reaches None 1 step earlier, switches to b1,
#   and then lands right on c1 at the exact same moment current2 (after switching to a1) lands on c1.

def find_merge_node(head1, head2):
    if head1 is None or head2 is None:
        return None
    
    current1 = head1
    current2 = head2
    
    while current1 is not current2:
        current1 = current1.next if current1 is not None else head2
        current2 = current2.next if current2 is not None else head1

    return current1.data if current1 is not None else None

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        test_case_count = int(input().strip())
        
        for _ in range(test_case_count):
            index = int(input().strip())
            
            l1_count = int(input().strip())
            l1 = SinglyLinkedList()
            
            for _ in range(l1_count):
                l1.insert_node(int(input().strip()))
                
            l2_count = int(input().strip())
            l2 = SinglyLinkedList()
            
            for _ in range(l2_count):
                l2.insert_node(int(input().strip()))
                
            ptr1 = l1.head;
            ptr2 = l2.head;

            for i in range(l1_count):
                if i < index:
                    ptr1 = ptr1.next
                    
            for i in range(l2_count):
                if i != l2_count-1:
                    ptr2 = ptr2.next

            ptr2.next = ptr1
            
            result = find_merge_node(l1.head, l2.head)
            file.write(str(result) + '\n')
