#!/bin/python3

# Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0.
# The list may be empty after you delete the node. In that case, return a null value.
#
# Example
# llist = 0 -> 1 -> 2 -> 3
# position = 2
#
# After removing the node at position 2, llist' = 0 -> 1 -> 3.
#
# Function Description
# Complete the deleteNode function in the editor below.
#
# deleteNode has the following parameters:
# - SinglyLinkedListNode pointer llist: a reference to the head node in the list
# - int position: the position of the node to remove
#
# Returns
# - SinglyLinkedListNode pointer: a reference to the head of the modified list
#
# Input Format
# The first line of input contains an integer n, the number of elements in the linked list.
# Each of the next n lines contains an integer, the node data values in order.
# The last line contains an integer, position, the position of the node to delete.
#
# Constraints
# - 1 <= n <= 1000
# - 1 <= list[i] <= 1000, where list[i] is the i^th element of the linked list.
#
# Sample Input
# 8
# 20
# 6
# 2
# 19
# 7
# 4
# 15
# 9
# 3
#
# Sample Output
# 20 6 2 7 4 15 9

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.delete_node

import os

from data_structure.singly_linked_list import SinglyLinkedList
from linked_list.print_linked_list import print_singly_linked_list

def delete_node(head, position):
    if not head:
        return head
    
    if position == 0:
        return head.next
    
    current = head
    current_position = 1
    
    while current:
        
        if current_position == position:
            current.next = current.next.next
            break
        
        current = current.next
        current_position += 1
    
    return head

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        count = int(input().strip())
        
        l = SinglyLinkedList()
        
        for _ in range(count):
            l.insert_node(int(input().strip()))
        
        position = int(input().strip())
        
        l.head = delete_node(l.head, position)
            
        print_singly_linked_list(l.head)
        file.write('\n')
