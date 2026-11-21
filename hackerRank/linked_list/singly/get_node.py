#!/bin/python3

# Given a pointer to the head of a linked list and a specific position, determine
# the data value at that position. Count backwards from the tail node. The tail is
# at postion 0, its parent is at 1 and so on.
#
# Example
# head refers to 3 -> 2 -> 1 -> 0 -> NULL
# positionFromTail = 2
#
# Each of the data values matches its distance from the tail. The value 2 is at
# the desired position.
#
# Function Description
# Complete the getNode function in the editor below.
#
# getNode has the following parameters:
# - SinglyLinkedListNode pointer head: refers to the head of the list
# - int positionFromTail: the item to retrieve
#
# Returns
# - int: the value at the desired position
#
# Input Format
# The first line contains an integer t, the number of test cases.
#
# Each test case has the following format:
# The first line contains an integer n, the number of elements in the linked list.
# The next n lines contains an integer, the data value for an element of the
# linked list.
# The last line contains an integer positionFromTail, the position from the
# tail to retrieve the value of.
#
# Constraints
# - 1 <= t <= 10
# - 1 <= n, m <= 1000
# - 1 <= list[i] <= 1000, where list[i] is the i^th element of the linked list.
# - 0 <= positionFromTail < n
#
# Sample Input
# 2
# 1
# 1
# 0
# 3
# 3
# 2
# 1
# 2
#
# Sample Output
# 1
# 3

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.get_node

import os

from data_structure.singly_linked_list import SinglyLinkedList

def get_node(head, position_from_tail):
    leader = head
    follower = head
    
    for _ in range(position_from_tail):
        leader = leader.next
        
    while leader.next is not None:
        leader = leader.next
        follower = follower.next
        
    return follower.data
    
if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        test_case_count = int(input().strip())
        
        for _ in range(test_case_count):
            count = int(input().strip())
            
            l = SinglyLinkedList()
            
            for _ in range(count):
                l.insert_node(int(input().strip()))
            
            position = int(input().strip())
            
            result = get_node(l.head, position)
            file.write(str(int(result)) + '\n')
