#!/bin/python3

# This exercise focuses on traversing a linked list. You are given a pointer to
# the head node of a linked list. The task is to print the data of each node,
# one per line. If the head pointer is null, indicating the list is empty,
# nothing should be printed.
#
# Function Description
# Complete the printLinkedList function with the following parameter(s):
# - SinglyLinkedListNode head: a reference to the head of the list
#
# Print
# - For each node, print its data value on a new line (console.log in
#   Javascript).
#
# Input Format
# The first line of input contains n, the number of elements in the linked list.
# The next n lines contain one element each, the data values for each
# node.
#
# Note: Do not read any input from stdin/console. Complete the
# printLinkedList function in the editor below.
#
# Constraints
# - 1 <= n <= 1000
# - 1 <= list[i] <= 1000, where list[i] is the i^th element of the linked list.
#
# Sample Input
# STDIN   Function
# -----   --------
# 2       n = 2
# 16      first data value = 16
# 13      second data value = 13
#
# Sample Output
# 16
# 13

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.print_linked_list

from data_structure.singly_linked_list import SinglyLinkedList

def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next

if __name__ == '__main__':
    count = int(input())

    l = SinglyLinkedList()

    for _ in range(count):
        item = int(input())
        l.insert_node(item)

    printLinkedList(l.head)
