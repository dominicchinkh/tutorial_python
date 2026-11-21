#!/bin/python3

# You're given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check
# if they are equal. If all data attributes are equal and the lists are the same length, return 1. Otherwise, return 0.
#
# Example
# llist1 = 1 -> 2 -> 3 -> NULL
# llist2 = 1 -> 2 -> 3 -> 4 -> NULL
#
# The two lists have equal data attributes for the first 3 nodes. llist2 is longer, though, so the lists are not equal. Return 0.
#
# Function Description
# Complete the compare_lists function in the editor below.
#
# compare_lists has the following parameters:
# - SinglyLinkedListNode llist1: a reference to the head of a list
# - SinglyLinkedListNode llist2: a reference to the head of a list
#
# Returns
# - int: return 1 if the lists are equal, or 0 otherwise
#
# Input Format
# The first line contains an integer t, the number of test cases.
#
# Each of the test cases has the following format:
# The first line contains an integer n, the number of nodes in the first linked list.
# Each of the next n lines contains an integer, each a value for a data attribute.
# The next line contains an integer m, the number of nodes in the second linked list.
# Each of the next m lines contains an integer, each a value for a data attribute.
#
# Constraints
# - 1 <= t <= 10
# - 1 <= n, m <= 1000
# - 1 <= llist1[i], llist2[i] <= 1000
#
# Output Format
# Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to
# stdout/console.
#
# The output is handled by the code in the editor and it is as follows:
# For each test case, in a new line, print 1 if the two lists are equal, else print 0.
#
# Sample Input
# 2
# 2
# 1
# 2
# 1
# 1
# 2
# 1
# 2
# 2
# 1
# 2
#
# Sample Output
# 0
# 1

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.compare_lists

import os

from data_structure.singly_linked_list import SinglyLinkedList

def compare_lists(head1, head2):
    
    current1 = head1
    current2 = head2
    
    while current1 is not None or current2 is not None:
        if current1 is None or current2 is None:
            return 0
        
        if current1.data != current2.data:
            return 0
        
        current1 = current1.next
        current2 = current2.next
    
    return 1

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
                
            result = compare_lists(list1.head, list2.head)
            
            file.write(str(int(result)) + '\n')
