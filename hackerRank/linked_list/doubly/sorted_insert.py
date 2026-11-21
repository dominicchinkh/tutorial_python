#!/bin/python3

# Given a reference to the head of a doubly-linked list and an integer, data, create a new DoublyLinkedListNode object
# having data value data and insert it at the proper location to maintain the sort.[cite: 9]
#
# Example
# head refers to the list 1 <-> 2 <-> 4 -> NULL[cite: 9]
# data = 3[cite: 9]
#
# Return a reference to the new list: 1 <-> 2 <-> 3 <-> 4 -> NULL.[cite: 9]
#
# Function Description
# Complete the sortedInsert function in the editor below.[cite: 9]
#
# sortedInsert has two parameters:[cite: 9]
# - DoublyLinkedListNode pointer head: a reference to the head of a doubly-linked list[cite: 9]
# - int data: An integer denoting the value of the data field for the DoublyLinkedListNode you must insert into the list.[cite: 9]
#
# Returns
# - DoublyLinkedListNode pointer: a reference to the head of the list[cite: 9]
#
# Note: Recall that an empty list (i.e., where head = NULL) and a list with one element are sorted lists.[cite: 9]
#
# Input Format
# The first line contains an integer t, the number of test cases.[cite: 9]
#
# Each of the test case is in the following format:[cite: 9]
# - The first line contains an integer n, the number of elements in the linked list.[cite: 9]
# - Each of the next n lines contains an integer, the data for each node of the linked list.[cite: 9]
# - The last line contains an integer, data, which needs to be inserted into the sorted doubly-linked list.[cite: 9]
#
# Constraints
# - 1 <= t <= 10[cite: 9]
# - 1 <= n <= 1000[cite: 9]
# - 1 <= DoublyLinkedListNode.data <= 1000[cite: 9]
#
# Sample Input
# STDIN   Function
# -----   --------
# 1       t = 1[cite: 10]
# 4       n = 4[cite: 10]
# 1       node data values = 1, 3, 4, 10[cite: 10]
# 3[cite: 10]
# 4[cite: 10]
# 10[cite: 10]
# 5       data = 5[cite: 10]
#
# Sample Output
# 1 3 4 5 10[cite: 10]

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.doubly.sorted_insert

import os

from data_structure.doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode
from linked_list.print_linked_list import print_doubly_linked_list

def sorted_insert(head, data):
    node = DoublyLinkedListNode(data)
    
    if not head:
        return node
    
    if data <= head.data:
        node.next = head
        head.prev = node
        return node
    
    current = head
    
    while current.next is not None and current.next.data < data:
        current = current.next

    if current.next is not None:
        node.next = current.next
        current.next.prev = node

    node.prev = current
    current.next = node
    
    return head

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        test_case_count = int(input().strip())
        
        for _ in range(test_case_count):
            count = int(input().strip())
            
            l = DoublyLinkedList()
            
            for _ in range(count):
                l.insert_node(int(input().strip()))
    
            data = int(input().strip())
            
            head = sorted_insert(l.head, data)
            
            print_doubly_linked_list(head, ' ', file)
            file.write('\n')
