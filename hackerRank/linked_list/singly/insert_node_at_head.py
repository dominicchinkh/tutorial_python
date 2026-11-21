#!/bin/python3

# Given a pointer to the head of a linked list, insert a new node before the
# head. The next value in the new node should point to head and the data
# value should be replaced with a given value. Return a reference to the new
# head of the list. The head pointer given may be null meaning that the
# initial list is empty.
#
# Function Description
# Complete the function insertNodeAtHead with the following
# parameter(s):
# - SinglyLinkedListNode llist: a reference to the head of a list
# - data: the value to insert in the data field of the new node
#
# Input Format
# The first line contains an integer n, the number of elements to be inserted
# at the head of the list.
# The next n lines contain an integer each, the elements to be inserted, one
# per function call.
#
# Constraints
# - 1 <= n <= 1000
# - 1 <= list[i] <= 1000
#
# Sample Input
# STDIN   Function
# -----   --------
# 5       n = 5
# 383     data items to insert 383 ... 321
# 484
# 392
# 975
# 321
#
# Sample Output
# 321
# 975
# 392
# 484
# 383

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.insert_node_at_head

import os

from data_structure.singly_linked_list import SinglyLinkedList, SinglyLinkedListNode
from linked_list.print_linked_list import print_singly_linked_list

def insert_node_at_head(head, data):
    node = SinglyLinkedListNode(data)
    node.next = head
    return node

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        count = int(input().strip())
        
        l = SinglyLinkedList()
        
        for _ in range(count):
            head = insert_node_at_head(l.head, int(input().strip()))
            l.head = head
        
        print_singly_linked_list(l.head)
        file.write('\n')
