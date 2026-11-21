#!/bin/python3

# Given a pointer to the head node of a linked list and an
# integer to insert at a certain position, create a new node with
# the given integer as its data attribute, insert this node at the
# desired position, and return the head node.
#
# A position of 0 indicates the head, a position of 1 indicates
# one node away from the head, and so on. The head pointer
# given may be null, meaning that the initial list is empty.
#
# Example
# head refers to the first node in the list 1 -> 2 -> 3
# data = 4
# position = 2
#
# Insert a node at position 2 with data = 4. The new list is
# 1 -> 2 -> 4 -> 3
#
# Function Description
# Complete the function insertNodeAtPosition with the
# following parameters:
# - SinglyLinkedListNode pointer llist: a reference to
#   the head of the list
# - data: an integer value to insert as data in the new node
# - position: an integer position to insert the new node, zero-
#   based indexing
#
# Returns
# - SinglyLinkedListNode pointer: a reference to the
#   head of the revised list
#
# Input Format
# The first line contains an integer n, the number of elements in
# the linked list.
# Each of the next n lines contains an integer
# SinglyLinkedListNode[i].data.
# The next line contains an integer data, the data of the node
# that is to be inserted.
# The last line contains an integer position.
#
# Constraints
# - 1 <= n <= 1000
# - 1 <= SinglyLinkedListNode[i].data <= 1000, where
#   SinglyLinkedListNode[i] is the i^th element of the
#   linked list.
# - 0 <= position <= n.
#
# Sample Input
# STDIN   Function
# -----   --------
# 3       n = 3
# 16      llist = 16->13->7
# 13
# 7
# 1       data = 1
# 2       position = 2
#
# Sample Output
# 16 13 1 7

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.insert_node_at_position

import os

from data_structure.singly_linked_list import SinglyLinkedList, SinglyLinkedListNode
from linked_list.print_linked_list import print_singly_linked_list

def insert_node_at_position(head, data, position):
    node = SinglyLinkedListNode(data)
    
    if position == 0:
        node.next = head
        head = node
    else:
        current = head
        current_position = 1
        
        while current:
            
            if current_position == position:
                node.next = current.next
                current.next = node
                break
            
            current_position += 1
            current = current.next
        
    return head

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        count = int(input().strip())
        
        l = SinglyLinkedList()
        
        for _ in range(count):
            l.insert_node(int(input().strip()))
        
        data = int(input().strip())
        position = int(input().strip())
        
        l.head = insert_node_at_position(l.head, data, position)
        
        print_singly_linked_list(l.head)
        file.write('\n')
