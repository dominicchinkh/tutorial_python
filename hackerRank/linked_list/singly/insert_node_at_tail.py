#!/bin/python3

# You are given the pointer to the head node of a linked list and an integer
# to add to the list. Create a new node with the given integer. Insert this
# node at the tail of the linked list and return the head node of the linked list
# formed after inserting this new node. The given head pointer may be null,
# meaning that the initial list is empty.
#
# Function Description
# Complete the insertNodeAtTail function with the following
# parameters:
# - SinglyLinkedListNode pointer head: a reference to the head of a
#   list
# - int data: the data value for the node to insert
#
# Returns
# - SinglyLinkedListNode pointer: reference to the head of the
#   modified linked list
#
# Input Format
# The first line contains an integer n, the number of elements in the linked
# list.
# The next n lines contain an integer each, the value that needs to be
# inserted at tail.
#
# Constraints
# - 1 <= n <= 1000
# - 1 <= list_i <= 1000
#
# Sample Input
# STDIN   Function
# -----   --------
# 5       size of linked list n = 5
# 141     linked list data values 141..474
# 302
# 164
# 530
# 474
#
# Sample Output
# 141
# 302
# 164
# 530
# 474

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.insert_node_at_tail

import os

from data_structure.singly_linked_list import SinglyLinkedList, SinglyLinkedListNode
from linked_list.print_linked_list import print_singly_linked_list

def insert_node_at_tail(head, data):
    node = SinglyLinkedListNode(data)
    
    if not head:
        return node
    
    current = head
    while current.next:
        current = current.next
        
    current.next = node
    return head

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        count = int(input().strip())
        
        l = SinglyLinkedList()
        
        for _ in range(count):
            head = insert_node_at_tail(l.head, int(input().strip()))
            l.head = head
            
        print_singly_linked_list(l.head)
        
